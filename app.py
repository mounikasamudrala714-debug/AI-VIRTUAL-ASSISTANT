from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

FRONTEND_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "frontend"
)

@app.route("/")
def home():
    return send_from_directory(FRONTEND_FOLDER, "index.html")

@app.route("/style.css")
def style():
    return send_from_directory(FRONTEND_FOLDER, "style.css")

@app.route("/script.js")
def script():
    return send_from_directory(FRONTEND_FOLDER, "script.js")

@app.route("/flower.jpg")
def flower():
    return send_from_directory(FRONTEND_FOLDER, "flower.jpg")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data["message"].lower()

    if "hello" in message or "hi" in message:
        reply = "Hello! Nice to meet you."

    elif "time" in message:
        reply = datetime.now().strftime("%I:%M:%S %p")

    elif "date" in message:
        reply = datetime.now().strftime("%d-%m-%Y")

    elif "who are you" in message:
        reply = "I am your AI Virtual Assistant."

    elif "bye" in message:
        reply = "Goodbye! Have a wonderful day."

    else:
        reply = "Sorry, I do not understand that yet."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)