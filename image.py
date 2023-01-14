from PIL import Image
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import numpy as np

def handle_image(bot):
    @bot.message_handler(commands=['image'])
    def send_image(message):
        # Create data for the graph
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Create the graph
        plt.plot(x, y)

        # Save the graph to a buffer
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        bot.send_photo(message.chat.id, buf)