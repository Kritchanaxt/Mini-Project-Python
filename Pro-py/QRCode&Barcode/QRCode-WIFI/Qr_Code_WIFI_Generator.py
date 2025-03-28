
import wifi_qrcode_generator as qr
from PIL import Image

qr_code = qr.wifi_qrcode('Name WIFI', False, 'WPA', 'Password')

qr_image = qr_code.make_image(fill_color="black", back_color="white")

qr_image.save("outputwifiqr.png", "PNG")

Image.open('outputwifiqr.png').show()
