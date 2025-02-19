from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace with your actual bot token
TOKEN = "7825732428:AAGsljAfTisZpMEq-jZatqFG3zyxu_9jN3U"
LOGO_URL = "https://drive.google.com/file/d/1_8A6AQEXtsLdbMN8m7F_W198ThhfMU81/view?usp=sharing"  # Replace with your actual logo URL

# Function to handle the /start command
async def start(update: Update, context):
    """Sends a welcome message with buttons and a logo image."""
    chat_id = update.message.chat_id

    # Define the buttons
    keyboard = [
        [InlineKeyboardButton("AI Trade", url="https://your-website.com/ai-trade")],
        [InlineKeyboardButton("AI Signal", url="https://your-website.com/ai-signal")],
        [InlineKeyboardButton("Deepseek", url="https://your-website.com/deepseek")],
        [InlineKeyboardButton("ChatGPT", url="https://your-website.com/chatgpt")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the logo and message
    await context.bot.send_photo(
        chat_id=chat_id,
        photo=LOGO_URL,
        caption="🚀 Welcome to our AI-powered bot! Choose an option below:",
        reply_markup=reply_markup,
    )

# Main function to run the bot
def main():
    """Start the bot."""
    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))

    # Start the bot
    app.run_polling()

if __name__ == "__main__":
    main()
