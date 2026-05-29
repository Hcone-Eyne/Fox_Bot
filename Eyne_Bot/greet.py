
from Security_keys.config import Boss_id
from Tele_Memory.brain import save_memory
# handles acess for specfic user
def is_boss(message):
    # if user id matches boss id
    if message.from_user.id == Boss_id:
        return True
    # else return false
    else:
        print(f"Unauthorized Access from User ID: {message.from_user.id}")
        return False





# handles greet function
def greet(bot,message,current_memory):

    if is_boss(message):
        # fetch data from memory
        name_in_memory = current_memory["user_name"]
        # update memory of system status to online 
        current_memory["system_status"] = "Online"
        # stores memory
        save_memory(current_memory)
        bot.send_message(message.chat.id,f"Hello,{name_in_memory}")
        
    # else send access denied
    else:
        bot.send_message(message.chat.id,"Access Denied.")