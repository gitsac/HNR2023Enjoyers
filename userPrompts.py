
from init_bot import bot
from finDb import addMember
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from finDb import addOweTransaction, people

def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 2
    markup.add(
        InlineKeyboardButton("I owe someone money", callback_data = "i-owe"),
        InlineKeyboardButton("Someone owe me", callback_data = "someone-owe"),
        InlineKeyboardButton("Add User", callback_data = "addUser")
    )
    return markup

def markup_users():
    markup = InlineKeyboardMarkup()
    markup.width = 2

    allUsersButtons = []
    for person in people:
        allUsersButtons.append(InlineKeyboardButton(person, callback_data = person))
    markup.add(*allUsersButtons)

    return markup

@bot.message_handler(commands=['config'])
def config(message):
    bot.reply_to(message, "Config mode", reply_markup = markup_inline())

amount = -1
user = "myself"

@bot.callback_query_handler(func=lambda callback: callback.data)
def callback_query(call):
    oweMode = False
    if call.data == "i-owe":
        oweMode = True
        bot.send_message(call.message.chat.id, text = "Who do you owe?", reply_markup = markup_users())
    elif call.data == "someone-owe":
        oweMode = False
        bot.send_message(call.message.chat.id, text = "Who owes you?", reply_markup = markup_users())
    elif call.data == "addUser":
        msg = bot.send_message(call.message.chat.id, "Who is being added?")
        bot.register_next_step_handler(msg, addUserToPeople)
    elif call.data == "amount":
        msg = bot.send_message(call.message.chat.id, "What is the amount?")
        bot.register_next_step_handler(msg, handleAmount)
    else: 
        if call.data in people:
            if oweMode:
                handleIOwe(user, call.data, amount)
                bot.send_message(call.message.chat.id, text = "you owe " + call.data + " " + str(amount)) 
            else: 
                handleSomeoneOwe(user, call.data, amount)
                bot.send_message(call.message.chat.id, text = call.data + " owes you" + " " + str(amount)) 

def handleIOwe(name1, name2, amount):
    addOweTransaction(name1, name2, amount) 

def handleSomeoneOwe(name1, name2, amount):
    addOweTransaction(name2, name1, amount)

def addUserToPeople(message):
    addMember(message.text)

def handleAmount(message):
    global amount
    amount = message.text

