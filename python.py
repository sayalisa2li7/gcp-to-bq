from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "data-flow-419812"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
    "jobName": "bq-load-613",  # Provide a unique name for the job
    "parameters": {
        "javascriptTextTransformGcsPath": "gs://data-flow-613/udf.js",
        "JSONPath": "gs://data-flow-613/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "data-flow-419812:diabetes_data.diabetes_data",
        "inputFilePattern": "gs://data-flow-613/diabetes_data.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://data-flow-613"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)