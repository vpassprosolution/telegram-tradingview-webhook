from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = "7825732428:AAGsljAfTisZpMEq-jZatqFG3zyxu_9jN3U"

async def start(update: Update, context):
    await update.message.reply_text("Hello! Your bot is working!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running... Press Ctrl+C to stop.")
app.run_polling()
