import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)
NEXT_URL = os.getenv("NEXT_URL", "<http://api:8080>")
VERSION = os.getenv("VERSION", "v1")

@app.route("/")
def index():
    try:
        downstream = requests.get(f"{NEXT_URL}/api", timeout=3).json()
    except Exception as e:
        downstream = {"error": str(e)}
    return jsonify(service="frontend", version=VERSION, downstream=downstream)

@app.route("/healthz")
def health():
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)