from init_bot import bot
import telebot
from finDb import addOweTransaction

@bot.message_handler(commands=['start'])
# def check_made(groupID):
    #Check if the groupID has already been initialized, if yes, then call get_action immediately. Else, call initialization

# def initialization(groupID, message):
#     #"Create" an object with the groupID, then collect the members' name
#     text="How many members will be involved?"
#     toSend = bot.send_message(message.chat.id, text)
#     bot.register_next_step_handler(toSend, iterThru)

# def iterThru(message):
#     listToUse = []

#     def addNames(msg):
#         useThisToAdd = msg.text
#         listToUse.append(useThisToAdd)


#     numOfMembers = message.text

#     for i in range(numOfMembers):
#         text = "What is the name of Member " + i + "?"
#         addToList = bot.send_message(message.chat.id, text)
#         bot.register_next_step_handler(addToList, addNames)

        

    


def get_action(message):
        text = "Do you owe someone money, or does someone owe you money?"
        # sent_msg = bot.send_message(message.chat.id, text, parse_mode = "Markdown")
        # bot.register_next_step_handler(sent_msg, identifyAction)
        keyboardToReply = telebot.types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard=True, one_time_keyboard=True)
        keyboardOweOption = telebot.types.InlineKeyboardButton("I owe someone money", callback_data = 'owe-people')
        keyboardPayOption = telebot.types.InlineKeyboardButton("Someone owes me money", callback_data = 'gain-people')
        keyboardToReply.add(keyboardOweOption, keyboardPayOption)
        bot.send_message(chat_id = message.chat.id, text = text, reply_markup=keyboardToReply)
        # keyboardWithMembers = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        # Use a for-loop to add members of this group into the keyboard, then allow the person to choose who is involved.

# @bot.callback_query_handler(func=lambda call:True)
# def identifyAction(dataIn):
#     dataToUse = dataIn.data
#     if (dataToUse.startsWith('owe-')):
#         # Call function in finDB, user = person1, other guy = person 2
#         addOweTransaction()
#     elif (dataToUse.startsWith('gain-')):
#         # Call function in finDB, user = person2, other guy = person 1
#         addOweTransaction()
    

