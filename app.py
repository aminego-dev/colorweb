# app.py
import os
from flask import Flask

app = Flask(__name__)

VERSION = os.environ.get("APP_VERSION", "1.0")
COLOR   = os.environ.get("APP_COLOR",   "#4A90D9")

@app.route("/")
def home():
    hostname = os.environ.get("HOSTNAME", "localhost")
    return f"""
    <html>
      <body style="background:{COLOR}; font-family:sans-serif; color:white; padding:60px; text-align:center;">
        <h1>colorweb v{VERSION}</h1>
        <p>Running on: <strong>{hostname}</strong></p>
        <p>Change APP_VERSION and APP_COLOR env vars to update me.</p>
      </body>
    </html>
    """, 200

@app.route("/health")
def health():
    return {"status": "ok", "version": VERSION}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
