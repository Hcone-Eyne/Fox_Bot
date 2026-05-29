# import libirary

# The Universal Import
import sys
from pathlib import Path
from dotenv import load_dotenv # type: ignore

master_root = Path(__file__).resolve().parent
env_root = master_root / "Security_keys" / ".env"

# Checking .env
if env_root.exists():
    load_dotenv(env_root)
else:
    print(f"Error Failed To Load: {env_root}")

# we use str because sys.append only accept string and path is not a string
sys.path.append(str(master_root))
sys.path.append(str(master_root / "Security_keys"))
sys.path.append(str(master_root / "Fox_Brain_Model"))
sys.path.append(str(master_root / "Tele_Memory"))


# assign value for Token
# initialise decocder "@"
# greet user with hello 

import telebot # type: ignore
import os
from Tele_Memory.brain import load_memory , save_memory   # type: ignore
from greet import is_boss,greet
from Security_keys.config import Boss_id  # type: ignore

import threading , time


master_path = Path(__file__).resolve().parent


Token = os.getenv("Token")
print(f"DEBUG: Looking for .env at: {env_root}")
print(f"DEBUG: Is the file there? {env_root.exists()}")
print(f"DEBUG: Token value is: {Token}")
if not Token:
    print("Error: Token not found in environment variables.")
    os._exit(1)

# Memory Space
current_memory = load_memory()

# checking memory
if "Error" in current_memory['system_status']:
    print(f"{current_memory['system_status']}")
else:
    print("Ready to Go! 🦇")

# timer
time_limit = 10
last_activity = time.time()

def session_checker():
    global last_activity
    while True:
        time.sleep(30)
        time_left = time.time() - last_activity
        if time_left > time_limit:
            print("Session timed out!")
            bot.send_message(Boss_id,"I'm Tired! Going to Sleep!")
            os._exit(0)
threading.Thread(target = session_checker , daemon = True).start()

# bot initialiser
bot = telebot.TeleBot(Token)

# Wake words
Wake_words = ["start", "hi", "hello", "hey fox", "fox", "fox?", "fox!"] 

# handles start command
@bot.message_handler(commands = ["start"])
@bot.message_handler(func = lambda message: any(word in message.text.lower() for word in Wake_words))
def initialiser_bot(message):
    global current_memory
    # getting time info for timer
    global last_activity
    last_activity = time.time()
    greet(bot,message,current_memory)


# importing Required Libraries
from julie_integration import julie_responses # type: ignore

# integration of Juile
@bot.message_handler(func = lambda message: True)
# Julie handles tasks such as seachning and normal conversation
def handler_of_messages(message):
    julie_responses(bot, message, current_memory)


# handles error
try:
    # print bot is online in terminal
    print("Bot Is Online...")
    # makes the bot listen for any incoming messages
    bot.infinity_polling()
# handles error   
except Exception as problem:
    # print error in terminal
    print(f"Error{problem}")
