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
