
from init_bot import bot
from finDb import addMember
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 2
    markup.add(
        InlineKeyboardButton("Add User", callback_data = "addUser")
    )
    return markup

@bot.message_handler(commands=['config'])
def config(message):
    bot.reply_to(message, "Config mode", reply_markup = markup_inline())

@bot.callback_query_handler(func=lambda callback: callback.data)
def callback_query(call):
    if call.data == "addUser":
        msg = bot.send_message(call.message.chat.id, "Who is being added?")
        bot.register_next_step_handler(msg, addUserToPeople)

def addUserToPeople(message):
    addMember(message.text)
    print(message.text)

