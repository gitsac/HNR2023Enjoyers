from init_bot import bot
from finDb import getImage

from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np

@bot.message_handler(commands=['image'])
def send_image(message):
    bot.send_photo(message.chat.id, getImage())