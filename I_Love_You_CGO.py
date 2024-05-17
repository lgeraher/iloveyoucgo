# ___          ___       ________  ___      ___ _______            ___    ___ ________  ___  ___          ________  ________  ________     
# |\  \        |\  \     |\   __  \|\  \    /  /|\  ___ \          |\  \  /  /|\   __  \|\  \|\  \        |\   ____\|\   ____\|\   __  \    
# \ \  \       \ \  \    \ \  \|\  \ \  \  /  / | \   __/|         \ \  \/  / | \  \|\  \ \  \\\  \       \ \  \___|\ \  \___|\ \  \|\  \   
#  \ \  \       \ \  \    \ \  \\\  \ \  \/  / / \ \  \_|/__        \ \    / / \ \  \\\  \ \  \\\  \       \ \  \    \ \  \  __\ \  \\\  \  
#   \ \  \       \ \  \____\ \  \\\  \ \    / /   \ \  \_|\ \        \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \____\ \  \|\  \ \  \\\  \ 
#    \ \__\       \ \_______\ \_______\ \__/ /     \ \_______\     __/  / /      \ \_______\ \_______\       \ \_______\ \_______\ \_______\
#     \|__|        \|_______|\|_______|\|__|/       \|_______|    |\___/ /        \|_______|\|_______|        \|_______|\|_______|\|_______|
#                                                                 \|___|/                                                                   

import json
import xmltodict
import boto3
import os
from pymongo import MongoClient

def lambda_handler(event, context):
    # S3 bucket and object details from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Initialize S3 client
    s3_client = boto3.client('s3')
    
    # Retrieve the XML file from S3
    xml_data = s3_client.get_object(Bucket=bucket_name, Key=object_key)['Body'].read().decode('utf-8')
    
    # Convert XML to JSON
    json_data = xml_to_json(xml_data)
    
    if json_data:
        print("JSON data generated successfully:")
        print(json_data)
        
        # Insert JSON data into MongoDB
        inserted_id = insert_to_mongo(json_data)
        print(f"Data inserted into MongoDB with ID: {inserted_id}")
    else:
        print("Failed to convert XML to JSON")

def xml_to_json(xml_str):
    try:
        # Parse the XML
        xml_dict = xmltodict.parse(xml_str)
        
        # Convert to JSON
        json_data = json.dumps(xml_dict, indent=4)
        return json_data
    
    except Exception as e:
        print(f"Error: {e}")
        return None

def insert_to_mongo(json_data):
    # Get MongoDB URI from environment variable
    mongo_uri = os.getenv('MONGO_URI')
    
    if not mongo_uri:
        raise ValueError("MONGO_URI environment variable is not set")
    
    # Create a MongoDB client
    client = MongoClient(mongo_uri)
    
    # Access the database
    db = client["purchase_orders"]
    
    # Access the collection
    collection = db["orders"]
    
    # Convert JSON string to Python dict
    data_dict = json.loads(json_data)
    
    # Insert the data into MongoDB
    result = collection.insert_one(data_dict)
    return result.inserted_id
