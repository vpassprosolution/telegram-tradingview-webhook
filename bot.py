from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace this with your actual Telegram bot token
TOKEN = "7825732428:AAGsljAfTisZpMEq-jZatqFG3zyxu_9jN3U"

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Get Trading Signals 📈", callback_data="signals")],
        [InlineKeyboardButton("Use Deepseek AI 🤖", callback_data="deepseek")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Choose an option:", reply_markup=reply_markup)

# Handle button clicks
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "signals":
        await query.message.reply_text("📡 Trading signals here soon!")
    elif query.data == "deepseek":
        await query.message.reply_text("🤖 Deepseek AI is coming soon!")

# Main function to start the bot
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
