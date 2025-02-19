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

from fastapi import FastAPI, Request
import json
import requests
import os

app = FastAPI()

TELEGRAM_BOT_TOKEN = os.getenv("7825732428:AAGsljAfTisZpMEq-jZatqFG3zyxu_9jN3U")  # Use your bot's token
CHAT_ID = os.getenv("6756668018")  # Replace with your chat ID or get it dynamically

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Received TradingView Alert:", data)  # Log the alert

    # Extract message from TradingView alert
    message = data.get("message", "No message received.")

    # Send message to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"📢 Trading Alert:\n{message}"}
    requests.post(telegram_url, json=payload)

    return {"status": "ok"}
