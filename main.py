# main.py - ÖRNEK (Basit Telegram botu, python-telegram-bot v13)
import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("TELEGRAM_TOKEN")  # Render'da env var olarak ekleyeceğiz

def start(update, context):
    update.message.reply_text("Bot çalışıyor ✅")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if name == "main":
    main()
