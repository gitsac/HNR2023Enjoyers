import telebot

def get_bot():
    BOT_TOKEN = '5800765511:AAFFwlHsRnV4sXPNh85y8GBK_tpn_HkhLEA'
    return telebot.TeleBot(BOT_TOKEN)