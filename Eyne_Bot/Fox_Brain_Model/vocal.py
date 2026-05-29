# declare all the required libary
import os
import json
import sys
from pathlib import Path


# getting things from parent directory
master_root = Path(__file__).resolve().parent
location = master_root.parent /"data"/ "train.txt"

# condition to check if train.txt is in use
if not os.path.exists(location):
    print("train.txt not found")
    print(location)
    exit()
else:
    print("train.txt found")
# open train.txt
with open(location,"r",encoding = "utf-8") as file:
    # read the file
    text = file.read()

char = sorted(list(set(text)))
vocab_size = len (char)

#initiaise the tokeniser
char_to_int = {}
int_to_char = {}

# adding special tokens (prevents crashs against emoji etc..) and replace them
if "<UNK>" not in char:
    char.append("<UNK>")
# checks and add padding token to match character value as nn excepts constant size of variable
if "<PAD>" not in char:
    char.append("<PAD>")

# tokeniser function
def tokeniser():
    for i,ch in enumerate(char):
        char_to_int[ch] = i
        int_to_char[i] = ch
# call tokeniser
tokeniser()

# save vocab_datas
vocab_data = {
    "char_to_int":char_to_int,
    "int_to_char":int_to_char,
    "vocab_size":vocab_size
    
}

vocab_path = os.path.join(os.path.dirname(__file__), "vocab.json")
with open(vocab_path, "w", encoding="utf-8") as file:
    json.dump(vocab_data, file)

print("All Clear Vocab_Data created Sucessfully")
print(f"Example: E is mapped to {char_to_int.get('E','N/A')}")
print(f"Vocab Size: {len(char_to_int)}")
print(f"UNK ID: {char_to_int['<UNK>']} -> {int_to_char[char_to_int['<UNK>']]}")