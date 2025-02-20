from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7825732428:AAGsljAfTisZpMEq-jZatqFG3zyxu_9jN3U
"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message with buttons."""
    keyboard = [
        [InlineKeyboardButton("AI Trade", callback_data="ai_trade")],
        [InlineKeyboardButton("AI Signal", callback_data="ai_signal")],
        [InlineKeyboardButton("Deepseek", callback_data="deepseek")],
        [InlineKeyboardButton("ChatGPT", callback_data="chatgpt")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Welcome! Choose an option:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks."""
    query = update.callback_query
    await query.answer()
    
    if query.data == "ai_trade":
        await query.message.reply_text("You selected AI Trade!")
    elif query.data == "ai_signal":
        await query.message.reply_text("You selected AI Signal!")
    elif query.data == "deepseek":
        await query.message.reply_text("You selected Deepseek!")
    elif query.data == "chatgpt":
        await query.message.reply_text("You selected ChatGPT!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot is running... Press Ctrl+C to stop.")
app.run_polling()
