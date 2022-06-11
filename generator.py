import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
s = input("Give me your data to crypt")
  
# Generate QR code 
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg" 
#url.svg("myqr.svg", scale = 8) 
  
# Create and save the png file naming "myqr.png"

url.png('testQrCode.png', scale = 6) 
'''
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Elyes Application')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="yellow")
'''
