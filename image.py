from PIL import Image
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import numpy as np
from finDb import getImage

def handle_image(bot):
    @bot.message_handler(commands=['image'])
    def send_image(message):
        bot.send_photo(message.chat.id, getImage())