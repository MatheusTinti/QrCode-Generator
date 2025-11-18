from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_base64 = None

    if request.method == "POST":
        texto = request.form["texto"]

        qr_img = qrcode.make(texto)

        img_buffer = io.BytesIO()
        qr_img.save(img_buffer, format="PNG")
        img_buffer.seek(0)

        qr_base64 = base64.b64encode(img_buffer.read()).decode("utf-8")

    return render_template("index.html", qr_base64=qr_base64)


app.run(host="0.0.0.0", port=5000, debug=True)
