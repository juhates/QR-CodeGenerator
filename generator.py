import pyqrcode

def qrcode():
    index = 0   # File name
    file = open('qr-codes.txt')     # File path
    for row in file:
        qr = pyqrcode.create(row)
        qr.png(str(index) + '.png', scale=6)
        index = index + 1
    print('QR Code Generation Completed...')
    
if __name__ == "__main__":
    qrcode()