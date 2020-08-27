
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

import numpy as np

import os
import argparse
import os
import ast
import pandas as pd
import json
from azure.servicebus import QueueClient,ServiceBusClient
from azureml.core import Run,Dataset, Workspace,Datastore
import joblib
from azureml.core.model import Model

def init():
    global sb_client, queue_client, aml_run,LGBM_MODEL, topic
    aml_run = Run.get_context()
    ws = aml_run.experiment.workspace
    keyvault = ws.get_default_keyvault()

    con_str =keyvault.get_secret('servicebustopic')

    sb_client = ServiceBusClient.from_connection_string(con_str)
    # queue_client = sb_client.get_queue("landing")
    #Loading model from AML Workspace

    model_name = "porto_seguro_safe_driver_model"
    model = Model(ws, model_name)
    model.download("model", exist_ok=True)
    model_path = os.path.join("model", model_name)
    LGBM_MODEL = joblib.load(model_path)
    parser = argparse.ArgumentParser()

    parser.add_argument("--topic", type=str,dest="topic", required=True, help="name of topic")

    args,_ = parser.parse_known_args()
    # Set number of tasks equal to total number of cores in the cluster
    topic = args.topic



def run(mini_batch):
    print(f'run method start: {__file__}, run({mini_batch})')
    resultList = []


    i=0
    for file in mini_batch:
        mini_batch_ds = pd.read_csv(file)
        msg_count = 0
        messages_to_fetch = int(mini_batch_ds.iloc[0]['messages_per_task'])
        subscription = str(mini_batch_ds.iloc[0]['subscription'])
        subscription_client=sb_client.get_subscription(subscription_name=subscription, topic_name =topic)

        print("processing batch ", i+1)
        print("files to score  for this batch",messages_to_fetch )

        #Preprocessing logic here for this batch
        with subscription_client.get_receiver(prefetch=10) as queue_receiver:

            while (msg_count<=messages_to_fetch):

                messages = queue_receiver.fetch_next(timeout=3, max_batch_size=10)
                for message in messages:
                    json_content = json.loads(str(message))
                    url = json_content['data']['url']
                    folder_name = url.split("/")[-2]
                    file_name = os.path.basename(url)
                    file_path=os.environ.get('AZUREML_DATAREFERENCE_datastore_sourcefiles_dir')+"/"+folder_name+"/"+file_name

                    print(url)

                    if ".csv" in url:
                        data = pd.read_csv(file_path)
                    elif ".xlsx" in url:
                        data = pd.read_excel(file_path)
                    else:
                        print("no suitable format to read")
                        continue
                    data =data.drop(['id'], axis=1)
                    try:
                        output = LGBM_MODEL.predict(data)
                    except Exception as e:
                        print("error predicting file {}".format(file_path), e)
                        continue
                    output = pd.DataFrame({"score": output, "source": [file_name] * len(output)})

                    target_file_name = file_name.replace("xlsx", "csv")
                    target_file_name= "scored_"+target_file_name

                    output_path = os.environ.get('AZUREML_DATAREFERENCE_batch_score_output')+"/"+folder_name

                    if  not os.path.exists(output_path):
                        os.mkdir(output_path)
                    print(" Folder name",folder_name)
                    output.to_csv(output_path+"/"+target_file_name)
                #dequeue the successfully processed messages.
                    message.complete()
                    msg_count+=1
        aml_run.log("{}".format(file.split("/")[-1].split(".")[0]), msg_count)
        resultList.append({"Number of files processed":msg_count})
        print("resultlist: ", resultList)
    return resultList




