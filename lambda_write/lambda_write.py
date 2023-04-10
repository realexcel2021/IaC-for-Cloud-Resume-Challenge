import json
import boto3
from decimal import Decimal

def lambda_handler(event, context):
    visit_count : int = 0
    body = json.loads(event['body'])
    the_id = body['value']


    dynamoDB = boto3.resource('dynamodb')
    table_name = "count_number"
    table = dynamoDB.Table(table_name)

    response = table.get_item(Key={"id" : the_id})

    if "Item" in response:
        visit_count = response['Item']['view_Count']

    visit_count += 1

    table.put_item(Item = {"id": the_id, "view_Count" : visit_count})
    
    return_value = Decimal(visit_count)
    
    return {
        'statusCode': 200,
         'body' : json.dumps(return_value, default=str)
    }
