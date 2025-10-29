from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # Allow frontend (React / RN / Vercel) requests

@app.route("/")
def home():
    return jsonify({"status": "success", "message": "Flask backend running on Render 🚀"})

@app.route("/api/test", methods=["GET"])
def test():
    return jsonify({"message": "API is working ✅"})

@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.json
    return jsonify({"received": data, "message": "POST request successful"})

if __name__ == "__main__":
    app.run(debug=True)
