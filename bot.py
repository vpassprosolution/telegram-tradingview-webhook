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
        "👋 Lets get try VPASS PRO V2 \n\nChoose an option below:",
        reply_markup=reply_markup
    )

keyboard = [[InlineKeyboardButton("Go to My Shop", url="https://myshop.com")]]



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



def ask_deepseek(user_message):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_message}],
        "temperature": 0.7  # Add temperature to control randomness
    }

    response = requests.post(url, json=data, headers=headers)

    print("Deepseek API Response:", response.text)  # Debugging line

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"  # Show error message


from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📊 Trading Signals", callback_data='signals')],
        [InlineKeyboardButton("📖 Learn More", callback_data='learn')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Welcome! Choose an option:", reply_markup=reply_markup)

dispatcher.add_handler(CommandHandler("start", start))



