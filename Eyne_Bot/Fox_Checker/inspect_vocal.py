# open train.txt
with open("train.txt","r", encoding = "utf-8") as file:
    # read train.txt
    text = file.read()
# get unique characters
char = sorted(list(set(text)))
# get Vocal char
vocab_size = len(char)

# print result  
print("Fox-Train-Vocab-Lab")
print("".join(char))
print(f"Total Unique Char {vocab_size}")