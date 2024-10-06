import qrcode


data = "https://www.youtube.com/watch?v=cEhnQN1ZmDI"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(back_color=(255,255,255), fill_color=(55, 95, 35))
img.save("qr_code.png")