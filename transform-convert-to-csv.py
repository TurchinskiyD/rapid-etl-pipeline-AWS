import json
import boto3
import pandas as pd

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    target_bucket = 'for-cleaned-data-bucket'
    target_file_name = object_key[:-5]

    waiter = s3_client.get_waiter('object_exists')
    waiter.wait(Bucket=source_bucket, Key=object_key)

    response = s3_client.get_object(Bucket=source_bucket, Key=object_key)

    data = response['Body'].read().decode('utf-8')
    data = json.loads(data)
    data_list = []
    for d in data['results']:
        data_list.append(d)
    df = pd.DataFrame(data_list)


    selected_columns = ['zipcode', 'city', 'homeType', 'homeStatus', 'livingArea',
                    'bathrooms', 'bedrooms', 'price', 'zestimate']
    df = df[selected_columns]

    csv_data = df.to_csv(index=False)

    bucket_name = target_bucket
    object_key = f"{target_file_name}.csv"
    s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=csv_data)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
