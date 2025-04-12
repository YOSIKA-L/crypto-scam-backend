from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/report", methods=["POST"])
def report():
    data = request.json
    domain = data.get("domain")
    timestamp = data.get("timestamp")

    with open("reported_scams.txt", "a") as f:
        f.write(f"{timestamp} - {domain}\n")

    return jsonify({"status": "success", "message": "Report received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
