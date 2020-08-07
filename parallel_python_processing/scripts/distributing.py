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
parser.add_argument("--core_per_node", type=int, help="number of cores per node")

parser.add_argument("--grouping_output", type=str, help="grouping_output")


args = parser.parse_args()
queue_length = args.queue_length

parallel_task_count = args.num_node*args.core_per_node
# This will create parallel_task_count tasks to run in parallel in a job run.
grouping_output_folder = args.grouping_output
if not (grouping_output_folder is None):
    os.makedirs(grouping_output_folder, exist_ok=True)
    print("%s created" % grouping_output_folder)

messages_per_task = int(queue_length/parallel_task_count)

#create a grouping of table:file_list
node_message_mapping = [messages_per_task]*parallel_task_count

map_output =pd.DataFrame({"messages_per_node":node_message_mapping})
dataset_path=os.path.join(grouping_output_folder,"mapping.csv")

map_output.to_csv(dataset_path)
