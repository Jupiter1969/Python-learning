# Author WenyuZheng

import json

file_name = 'json_test.json'

with open (file_name,'w') as file_object:
    json.dump('test',file_object)

with open (file_name) as file_object:
    text = json.load(file_object)
    print(text)