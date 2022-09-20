import os
import json

def save_file(file_path:str,dicts:dict)->None:
    file_name = 'result.json'
    file_path = os.path.join(file_path,file_name)
    #os.chdir(file_path)
    with open(file_path,'w') as file:
        json.dump(dicts,file, indent = 4)