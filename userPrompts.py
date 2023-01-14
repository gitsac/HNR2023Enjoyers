
from init_bot import bot
from finDb import addMember
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from finDb import addOweTransaction, people, wipedb

def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 2
    markup.add(
        InlineKeyboardButton("I owe someone money", callback_data = "i-owe"),
        InlineKeyboardButton("Someone owe me", callback_data = "someone-owe"),
        InlineKeyboardButton("I pay", callback_data = "pay"),
        InlineKeyboardButton("Add User", callback_data = "addUser"),
        InlineKeyboardButton("Clear data", callback_data= 'clear')
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

@bot.message_handler(commands=['start'])
def config(message):
    bot.reply_to(message, "Config mode", reply_markup = markup_inline())

amount = -1
user = "other"
me = "me"
oweMode = -1

@bot.callback_query_handler(func=lambda callback: callback.data)
def callback_query(call):
    global user
    global oweMode
    global me
    if call.data == "i-owe":
        oweMode = 0
        bot.send_message(call.message.chat.id, text = "Who do you owe?", reply_markup = markup_users())
    elif call.data == "someone-owe":
        oweMode = 1
        bot.send_message(call.message.chat.id, text = "Who owes you?", reply_markup = markup_users())
    elif call.data == "pay":
        oweMode = 2
        bot.send_message(call.message.chat.id, text = "Who have you paid?", reply_markup = markup_users())
    elif call.data == "addUser":
        msg = bot.send_message(call.message.chat.id, "Who is being added?")
        bot.register_next_step_handler(msg, addUserToPeople)
    elif call.data == 'clear':
        wipedb()
        bot.send_message(call.message.chat.id, "Database wiped")
    elif user == "other" and call.data in people:
        user = call.data
        bot.send_message(call.message.chat.id, text = "Who are you?", reply_markup = markup_users())
    else: 
        if call.data in people:
            me = call.data
            msg = bot.send_message(call.message.chat.id, text="What is the amount?")
            bot.register_next_step_handler(msg, handleAmount)

def handleIOwe(name1, name2, amount):
    addOweTransaction(name1, name2, amount) 

def handleSomeoneOwe(name1, name2, amount):
    addOweTransaction(name2, name1, amount)

def addUserToPeople(message):
    addMember(message.text)
    bot.send_message(message.chat.id, "Added success")

def handleAmount(message):
    global oweMode
    global user
    global me
    global amount
    amount = int(message.text)
    if oweMode == 0:
        handleIOwe(me, user, amount)
        bot.send_message(message.chat.id, text = me + " owe " + user + " " + str(amount)) 
    elif oweMode == 1: 
        handleSomeoneOwe(me, user, amount)
        bot.send_message(message.chat.id, text = user + " owes " + me + " " + str(amount)) 
    else: 
        handleIOwe(me, user, -1 * amount) 
        bot.send_message(message.chat.id, text = me + " paid " + user + " " + str(amount)) 

    user = "other"

