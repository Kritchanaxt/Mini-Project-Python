
import pyqrcode

link = input("Enter information QRCode: ")
qr_code = pyqrcode.create(link, encoding='utf-8')
qr_code.png("output.png", scale=6)
qr_code.show()
