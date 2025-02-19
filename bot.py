from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "7825732428:AAGsljAfTisZpMEq-jZatqFG3zyxu_9jN3U"

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("🔍 Deepseek Search", callback_data="deepseek_search")],
        [InlineKeyboardButton("📈 TradingView Signals", callback_data="tradingview_signals")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to the Trading Bot!\n\nChoose an option below:",
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "deepseek_search":
        await query.message.reply_text("🔍 Deepseek Search feature coming soon!")
    elif query.data == "tradingview_signals":
        await query.message.reply_text("📈 TradingView Signals integration coming soon!")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()



import requests
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Load environment variables
DEEPSEEK_API_KEY = "sk-96531fad1ab04ae59c1b5d76cb6aaf07"  # Replace with your actual API key
TELEGRAM_BOT_TOKEN = "7825732428:AAGsljAfTisZpMEq-jZatqFG3zyxu_9jN3U"  # Replace with your actual bot token

# Function to query Deepseek AI
def ask_deepseek(user_message):
    url = "https://api.deepseek.com/v1/chat/completions"  # Example URL, replace if needed
    headers = {
        "Authorization": f"Bearer {sk-96531fad1ab04ae59c1b5d76cb6aaf07}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_message}]
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Sorry, I couldn't process your request."

# Handle user messages
async def handle_message(update: Update, context):
    user_message = update.message.text
    response = ask_deepseek(user_message)
    await update.message.reply_text(response)

# Start command
async def start(update: Update, context):
    await update.message.reply_text("Welcome! Ask me anything using Deepseek AI.")

# Create bot application
app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Run bot
app.run_polling()
