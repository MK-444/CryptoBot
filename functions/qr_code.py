import qrcode
from dotenv import load_dotenv
import os
load_dotenv()


data= os.environ.get("BTC_ADDRESS") 
qr = qrcode.QRCode(version = 1,
            box_size = 7,
            border = 4)
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('functions/qrcodes/MyQRCode1.png')




