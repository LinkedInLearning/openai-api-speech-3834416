from io import BytesIO

from openai import OpenAI
from flask import Flask, render_template, send_file, request

client = OpenAI()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tts", methods=["POST"])
def tts():
    data = request.get_json()
    text = data.get("text", "")
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )
    return send_file(BytesIO(response.read()), mimetype="audio/mp3")


app.run(debug=True)
