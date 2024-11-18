import qrcode
import image
qr = qrcode.QRCode(
    version= 1,
    box_size = 10,
    border = 4 
)

data = input("enter your URL or some data :")
qr.add_data(data)
img = qr.make_image(fill = "black", back_color = "white")
img.save("newQRCode.png")
