import qrcode

texto = input("Digite o texto para gerar o QR Code: ")

img = qrcode.make(texto)

img.save("qrcode.png")

print("QR Code gerado com sucesso: qrcode.png")
