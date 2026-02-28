from flask import Flask, render_template, request, jsonify
from model import predict_category
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    name = data.get("name")
    location = data.get("location")
    message = data.get("message")

    if not name or not location or not message:
        return jsonify({"reply": "Please fill all fields."})

    category = predict_category(message)

    reply = (
        f"Thank you {name}. Your complaint about {category} at {location} "
        f"has been registered successfully."
    )

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)