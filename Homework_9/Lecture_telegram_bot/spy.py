import datetime

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    Updater,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
)


def log(update: Update, context: ContextTypes):
    with open("log.csv", "a", encoding="utf-8", newline="") as file:
        file.write(
            f"{datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')} - "
            f"{update.effective_user.first_name}, {update.effective_user.id}, "
            f"{update.message.text}\n")
