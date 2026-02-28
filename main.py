from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import Error
from model import predict_category

app = Flask(__name__)

# -------------------- MySQL Connection --------------------
try:
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="civicuser",
        password="1234",
        database="civic_project",
        auth_plugin="mysql_native_password"
    )

    if db.is_connected():
        print("✅ MySQL Connected Successfully")
        cursor = db.cursor()
    else:
        print("❌ MySQL Connection Failed")

except Error as e:
    print("❌ Database Error:", e)
    db = None
    cursor = None


# -------------------- Home Route --------------------
@app.route("/")
def home():
    return render_template("chat.html")


# -------------------- Chat Route --------------------
@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Safely get JSON data
        data = request.get_json()

        if not data:
            return jsonify({"reply": "Invalid request. Please try again."})

        name = data.get("name")
        location = data.get("location")
        description = data.get("message")

        # Validate input
        if not name or not location or not description:
            return jsonify({"reply": "Please fill all fields properly."})

        # AI Prediction
        category = predict_category(description)

        # Save to DB only if connected
        if db and db.is_connected():
            sql = """
                INSERT INTO complaints (name, location, description, category)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (name, location, description, category))
            db.commit()
        else:
            return jsonify({"reply": "Database connection error."})

        # Professional Reply
        reply = (
            f"Thank you {name}. "
            f"Your complaint regarding {category} at {location} has been registered successfully. "
            f"It will be resolved within 1-2 working days."
        )

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Server error: {str(e)}"})


# -------------------- Run Server --------------------
if __name__ == "__main__":
    app.run(debug=True)