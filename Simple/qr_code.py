import pyqrcode
url = 'https://github.com/John2208/Python-Projects'
k = pyqrcode.create(url)
k.png('GitQR.png',scale=10)