from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from flask import Flask, request
import requests

# Telegram Bot Token
TELEGRAM_TOKEN = "7825732428:AAGsljAfTisZpMEq-jZatqFG3zyxu_9jN3U"
DEEPSEEK_API_KEY = "sk-96531fad1ab04ae59c1b5d76cb6aaf07
"

# Initialize Flask app for TradingView webhook
app = Flask(__name__)

# Start command for Telegram bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! I am your trading signal bot.")

# Handle TradingView webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    signal = data.get('signal')  # Extract signal from TradingView alert
    send_signal_to_telegram(signal)
    return "OK", 200

# Send signal to Telegram
def send_signal_to_telegram(signal):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": "6756668018",  # Replace with your chat ID
        "text": f"New Signal: {signal}"
    }
    requests.post(url, json=payload)

# Integrate DeepSeek (example function)
def analyze_with_deepseek(data):
    url = "https://api.deepseek.com/analyze"  # Replace with DeepSeek API endpoint
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

# Main function to run the bot
def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    # Run Flask app for TradingView webhook
    app.run(port=5000)
    # Run Telegram bot
    main()