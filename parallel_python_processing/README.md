# Parallel Python Processing

The overall pipeline is an ADF pipeline has 2 steps:
- Web service step that retrieves the queue size from Azure Service Bus using this API: https://docs.microsoft.com/en-us/rest/api/servicebus/Queues/Get
- AML Pipeline with 2 steps on its own:
    1. Distributing: forming the input dataset which corresponds to number of parallel tasks (nodes * cores) for the parallel step
    2. Parallel execution: Launch multiple parallel tasks, each connect to Service Bus on its own and retrieve no more than a specified number of messages and process on its own
Setup:
- Setup a EventGrid trigger on a folder in a storage account. The storage account should has 2 main containers: landing and process. The landing is where files are landed. Files are uploaded according to following structure: landing/source/*.csv 
- Run the pipeline_definition notebook to build AML pipeline. At the end publish the AML Pipeline
- Setup ADF pipeline following the adf_pipeline.json definition with a web step and an AML pipeline step. In web step, need to generate authorization token.
An easy way to do this is go through try it button in https://docs.microsoft.com/en-us/rest/api/servicebus/Queues/Get then copy the token to use.
Token by default will expire after 1 hour
 
 

