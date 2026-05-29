''' This is used to Test if the bot can access web or not '''

# import library
from ddgs import DDGS # type: ignore

# function block to search web
with DDGS() as ddgs:
    for i in ddgs.text("Hello",max_result= 1):
        print(i)