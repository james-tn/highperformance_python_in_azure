import argparse
import os
import pandas as pd
import time
import ast
from azureml.core import Run,Datastore


parser = argparse.ArgumentParser()
# parser.add_argument("--data_folder", type=str, help="data folder argument")
parser.add_argument("--queue_length", type=int, help="length of the queue")
parser.add_argument("--num_node", type=int, help="number of nodes")
parser.add_argument("--grouping_output", type=str, help="grouping_output")


args = parser.parse_args()
# data_folder = args.data_folder
queue_length = args.queue_length
num_node = args.num_node
grouping_output_folder = args.grouping_output
if not (grouping_output_folder is None):
    os.makedirs(grouping_output_folder, exist_ok=True)
    print("%s created" % grouping_output_folder)

messages_per_node = int(queue_length/num_node)

#create a grouping of table:file_list
node_message_mapping = [messages_per_node]*num_node

map_output =pd.DataFrame({"messages_per_node":node_message_mapping})
dataset_path=os.path.join(grouping_output_folder,"mapping.csv")

map_output.to_csv(dataset_path)
