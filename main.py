from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "7825732428:AAGiFm1AOG-Xj_0C19_8cTeY2pT-ZFsHXaY"

async def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message with buttons when the user starts the bot."""
    keyboard = [
        [InlineKeyboardButton("Help", callback_data="help")],
        [InlineKeyboardButton("Info", callback_data="info")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to the bot! Choose an option below:",
        reply_markup=reply_markup
    )

def main():
    """Start the bot."""
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__": 
    main()    
