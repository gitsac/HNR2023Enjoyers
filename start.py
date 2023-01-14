def handle_start(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message, "Hello! How can I help you?")