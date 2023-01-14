from PIL import Image

def handle_image(bot):
    @bot.message_handler(commands=['image'])
    def send_image(message):
        image = Image.new('RGB', (100, 100), color = (73, 109, 137))
        bot.send_photo(message.chat.id, image)