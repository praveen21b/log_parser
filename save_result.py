import os
import json

def save_file(file_path:str,dicts:dict)->None:
    """ Save the result in json file"""
    file_name = 'result.json'
    file_path = os.path.join(file_path,file_name)
    with open(file_path,'w') as file:
        json.dump(dicts,file, indent = 4)