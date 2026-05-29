search_key_words = ["what is", "who is", "how to", "search", "find", "why does", "current price","can you","tell me","?","How","Who","When","Search up"]

def key_w_identifier(text):
    # converts into lower text
    text_string = text.lower()

    # checks if any keyword is present in the text
    keyword_found = False
    for keyword in search_key_words:
        if keyword in text_string:
            keyword_found = True
            break

    # check if normal or search conversation
    long_text = False
    word = text_string.split()
    if len(word) >= 8:
        long_text = True

    # returns the result
    if keyword_found or long_text:
        return "search"
    else:
        return "normal_conversation"
        
