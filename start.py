from init_bot import bot

@bot.message_handler(commands=['start'])
def handle(message):
    bot.reply_to(message, "Hello! How can I help you?")