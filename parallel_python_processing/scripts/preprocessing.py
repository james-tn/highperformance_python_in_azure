
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

def init():
    global queue_client
    run = Run.get_context()
    ws = run.experiment.workspace
    keyvault = ws.get_default_keyvault()

    con_str =keyvault.get_secret('servicebusconstr')

    sb_client = ServiceBusClient.from_connection_string(con_str)
    queue_client = sb_client.get_queue("landing")


def run(mini_batch):
    print(f'run method start: {__file__}, run({mini_batch})')
    resultList = []
    print("minibatch is ", mini_batch)
    messages_to_fetch= mini_batch['messages_per_task'][0]
    print("messages_to_fetch is", messages_to_fetch)

    msg_count=0


    #Preprocessing logic here for this batch
    while (msg_count<=int(messages_to_fetch)):

        with queue_client.get_receiver(prefetch=1000) as queue_receiver:
            messages = queue_receiver.fetch_next(timeout=30, max_batch_size=1000)
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


                target_file_name = file_name.replace("xlsx", "csv")

                output_path = os.environ.get('AZUREML_DATAREFERENCE_preprocess_output')+"/"+folder_name

                if  not os.path.exists(output_path):
                    os.mkdir(output_path)
                print(" Folder name",folder_name)
                data.to_csv(output_path+"/"+target_file_name)
            #dequeue the successfully processed messages.
                message.complete()
                msg_count+=1

        resultList.append(1)

    return resultList
# if __name__ == "__main__":
#     hello.helloworld("hello")



