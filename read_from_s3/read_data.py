import boto3
import requests
import json

s3_client = boto3.client("s3")


def read_data():

    #bucket name
    bucket = "star-wars-buckets"
    
    #file name in bucket
    key = "movie_cast.json"
    
    response = s3_client.get_object(Bucket = bucket, Key = key)["Body"]
    #converting response to json
    
    json_data = json.loads(response.read())


    return json_data
    
