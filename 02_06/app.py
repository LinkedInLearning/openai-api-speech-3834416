from io import BytesIO

from openai import OpenAI

client = OpenAI()


from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    if "file" not in request.files:
        return "No file part in the request", 400
    file = request.files["file"]
    file_like = BytesIO(file.read())
    file_like.name = file.filename
    print(file_like.name)

    transcript = client.audio.translations.create(
        model="whisper-1", 
        file=file_like,
    )
    return transcript.text


if __name__ == "__main__":
    app.run(debug=True)
