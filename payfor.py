from init_bot import bot
from finDb import addOweTransaction, userExists

@bot.message_handler(commands=['payfor'], chat_types=['group'])
def handle(message):
    payload = message.text.split()[1:]
    if len(payload) != 2:
        return bot.reply_to(message, f"Expected 2 arguments, got {len(payload)}.")
    user = message.from_user.username
    recipient = payload[0][1:]
    amount = float(payload[1])
    
    if (not userExists(user)):
        return bot.reply_to(message, f"@{user} is not registered")
    if (not userExists(recipient)):
        return bot.reply_to(message, f"@{recipient} is not registered")
    
    addOweTransaction(recipient, user, amount)
    bot.reply_to(
        message, 
        f"@{user} pays for @{recipient} ${amount:.2f}"
    )