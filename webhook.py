from flask import Flask, request
import requests

TOKEN = "7825732428:AAGiFm1AOG-Xj_0C19_8cTeY2pT-ZFsHXaY"
CHAT_ID = "6756668018"

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = f"📢 TradingView Alert:\n{data.get('message', 'No message received')}"
    
    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(telegram_url, json={"chat_id": CHAT_ID, "text": message})

    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
