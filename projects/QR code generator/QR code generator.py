import qrcode
import image

qr = qrcode.QRCode(version=8, box_size=10, border=5)

data = "https://www.panda3d.org/"

qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill="black", back_color="white")
image.save("/Users/winsorhoang/dev/python/projects/QR code generator/test.png")
print("QRCode generated")

