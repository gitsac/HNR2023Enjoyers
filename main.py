from init_bot import get_bot
from start import handle_start
from image import handle_image

bot = get_bot()
handle_start(bot)
handle_image(bot)

bot.polling()