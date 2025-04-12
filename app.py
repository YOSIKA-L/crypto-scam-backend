from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/report", methods=["POST"])
def report():
    data = request.json
    domain = data.get("domain")
    timestamp = data.get("timestamp", datetime.utcnow().isoformat())

    with open("reported_scams.txt", "a") as f:
        f.write(f"{timestamp} - {domain}\n")

    return jsonify({"status": "success", "message": "Report received"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
