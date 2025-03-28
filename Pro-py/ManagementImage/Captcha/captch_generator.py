
from captcha.image import ImageCaptcha
from PIL import Image

image = ImageCaptcha(width = 300, height = 100)
captcha_text = input("Set the message: ")
data = image.generate(captcha_text)
image.write(captcha_text, 'CAPTCHA.png')
Image.open('CAPTCHA.png')