from init_bot import bot

@bot.message_handler(commands=['payfor'], chat_types=['group'])
def handle(message):
    payload = message.text.split()[1:]
    if len(payload) != 2:
        return bot.reply_to(message, f"Expected 2 arguments, got {len(payload)}.")
    recipient = payload[0][1:]
    amount = float(payload[1])
    bot.reply_to(
        message, 
        f"@{message.from_user.username} pays for @{recipient} ${amount:.2f}"
    )