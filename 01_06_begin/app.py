from io import BytesIO

from openai import OpenAI
from flask import Flask, render_template, send_file, request

client = OpenAI()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")





app.run(debug=True)
