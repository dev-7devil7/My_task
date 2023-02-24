import json
from get_cast_details import *

def lambda_handler(event, context):

    api_url = "https://swapi.dev/api/films/"
    
    result_json = get_cast_details(api_url)

    return result_json
    
#lambda_handler(1,2)