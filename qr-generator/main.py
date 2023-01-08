import sys
import qrcode

codeValue = input("Enter QR code content: ")

print(
    """
Select error correction level
    L - up to 7% damage
    M - up to 15% damage
    Q - up to 25% damage
    H - up to 30% damage
    """
)
errorLevel = input('Enter letter: ')
while True:
    if errorLevel not in ['L', 'H', 'M', 'Q']:
        errorLevel = input('Incorrect input, please try again (L, H, M, Q): ')
    else:
        print('correct input selected')
        break

if errorLevel == 'L':
    error_correction = qrcode.constants.ERROR_CORRECT_L
elif errorLevel == 'H':
    error_correction = qrcode.constants.ERROR_CORRECT_H
elif errorLevel == 'M':
    error_correction = qrcode.constants.ERROR_CORRECT_M
elif errorLevel == 'Q':
    error_correction = qrcode.constants.ERROR_CORRECT_M
else:
    print('Error occur: error correction level is not selected!')
    sys.exit()

qrCode = qrcode.QRCode(
    version=1,
    error_correction=error_correction,
    box_size=10,
    border=4,
)
qrCode.add_data(codeValue)
qrCode.make(fit=True)
img = qrCode.make_image(fill_color="black", back_color="white")

type(img)
img.save("code.png")
