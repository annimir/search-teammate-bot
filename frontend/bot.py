from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я бот.")

def get_data(update: Update, context: CallbackContext):
    response = requests.get("http://server:8000/items/123")
    update.message.reply_text(f"Данные: {response.json()}")

updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("data", get_data))
updater.start_polling()