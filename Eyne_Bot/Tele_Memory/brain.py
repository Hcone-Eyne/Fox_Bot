# importing nessary libraries from python

import os
import json

# create a memory file
memory_file = "Fox_memory.json"

# save memory
def save_memory(current_data):
    with open(memory_file,"w") as file:
        return json.dump(current_data,file,indent=4)

# load memory
def load_memory():
    if os.path.exists(memory_file):
        with open(memory_file,"r") as file:
            return json.load(file)
    else:
        return {"user_name":"Enoch","system_status":"Info Isn't Stored Yet"}