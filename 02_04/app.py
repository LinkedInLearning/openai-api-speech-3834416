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
    transcript = "Place holder"
    
    return transcript


if __name__ == "__main__":
    app.run(debug=True)
