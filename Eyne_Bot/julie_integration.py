import sys
from pathlib import Path

# path to the websearch
master_root = Path(__file__).resolve().parent
access_root_web = master_root / "bot_tools" / "websearch.py"
access_root_router = master_root / "router.py"

sys.path.append(str(master_root))
sys.path.append(str(access_root_web))
sys.path.append(str(access_root_router))

from router import key_w_identifier # type: ignore
from bot_tools.websearch import web_searcher


# importing websearch
def julie_responses(bot, message, current_memory):
    # this fetch user input
    user_input = message.text

    # its kinda defensive where for example: if user sends image it won't process it
    if not user_input:
        bot.reply_to(message,"It Seems Like you Shared Something Else Boss..!\n Which isn't Readable By Me.")
        return

    # descision making using router / asking router
    decision = key_w_identifier(user_input)

    # building up conditions to react for seach and normal conversion based on router
    if decision == "search":
        print(f"DEBUG: Jullie is online: Fetching Info : {user_input}")
        bot.send_chat_action(message.chat.id,"typing")

        # fetch data from web
        data_fetcher = web_searcher(user_input)

        bot.reply_to(message,f"Here's The Required info Boss..\n\n{data_fetcher}")

    else:
        bot.reply_to(message,"Couldn't Find Info, Boss")

        
            