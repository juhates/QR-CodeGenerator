import pyqrcode

##############################################
# pip install pyqrcode
# pip install pypng

def qrcode():
    with open('qr-codes.txt', 'r') as file:
        for row in file:
            row = row.strip()  # Remove newline characters and leading/trailing whitespace
            # Replace invalid characters
            safe_filename = row.replace('/', '_').replace(':', '_')
            safe_filename = safe_filename.replace(
                'https___www.', '')  # Remove 'https___www.' part
            qr = pyqrcode.create(row)
            qr.png(safe_filename + '.png', scale=6)
    print('QR Code Generation Completed...')


if __name__ == "__main__":
    qrcode()
