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
    if not "file" in request.files:
        return "No file part in request.", 400
    file = request.files["file"] 
    file_like = BytesIO(file.read())
    file_like.name = file.filename
    transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=file_like, 
        response_format="text",
    )
    
    return transcript


if __name__ == "__main__":
    app.run(debug=True)
