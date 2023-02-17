from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}\n'
                                    f'I can:\n'
                                    f'/hi - поздароваюсь с тобой\n'
                                    f'/time - покажу текущее время\n'
                                    f'/sum x y - сложу два числа через пробел\n'
                                    f'/help - покажу доступные команды')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi - поздароваюсь с тобой\n'
                                    f'/time - покажу текущее время\n'
                                    f'/sum x y - сложу два числа через пробел\n'
                                    f'/help - покажу доступные команды')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')
