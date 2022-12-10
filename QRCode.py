#QR code Generator using "pyqrcode" module
import pyqrcode
from pyqrcode import QRCode
s = "This is the QR Code by Tushar Agrawal."
url = pyqrcode.create(s)
url.svg("QRCode.svg",scale=10)
