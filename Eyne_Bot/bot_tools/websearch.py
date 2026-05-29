# importing duckduckgo (google is kinda complecated rn)
from ddgs import DDGS # type: ignore
# function block to search web
def web_searcher(query):
    try:
        # assigning DDGS() to ddgs
        with DDGS() as ddgs:
            # searching the web
            result = ddgs.text(query, max_result=3)
            if not result:
                return "No Data Found in Web"
            # providing output by joining and making it as list as it has more alphabetic values to iterate
            context_block = "\n".join([temp_variable["body"] for temp_variable in result ])
            # returning context
            return context_block
    # preventing the error
    except Exception as e:
        print(f"Error:{e}")
        return "Web Error:{e}"