from io import BytesIO

from openai import OpenAI
from flask import Flask, render_template, send_file, request

client = OpenAI()
app = Flask(__name__)