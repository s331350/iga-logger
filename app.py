from flask import Flask, request
import json, os, datetime

app = Flask(__name__)
LOG_FILE = "iga_disable_log.jsonl"

@app.route("/upload", methods=["POST"])
def upload():
    try:
        data = request.get_json(force=True)
    except Exception:
        return {"error": "Invalid JSON"}, 400

    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        **data
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return {"ok": True, "entries": 1}

@app.route("/")
def index():
    return "<h3>IGA Logger attivo ✅</h3>", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
