from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *
from pyowm import OWM
from multiprocessing import context
import functions as func
import YTdwl as dwl




async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(f'/help - Показать команды\n/hi - Приветствие\n/time - Текущее время\n/sum - Сумма\n/mult - Умножение\n/sub - Вычитание\n/div - Деление\n/calc -Встроенный калькулятор\n/temp - Погода в указанном городе\n/dwl ссылка - скачать с YouTube')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()# /sum 123 3456
    x = int(items[1])
    y = int(items[2])

    await update.message.reply_text(f'{x}+{y} = {x+y}')

async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()# /sum 123 3456
    x = int(items[1])
    y = int(items[2])

    await update.message.reply_text(f'{x}*{y} = {x*y}')

async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()# /sum 123 3456
    x = int(items[1])
    y = int(items[2])

    await update.message.reply_text(f'{x}-{y} = {x-y}')

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()# /sum 123 3456
    x = int(items[1])
    y = int(items[2])

    await update.message.reply_text(f'{x}/{y} = {x/y}')

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    msg = update.message.text
    msg = msg.split(' ')

    
    print(msg)
    def funct(esp_str:str) -> int:
        par_close=esp_str.find(')')
        if par_close != -1:
            par_open = esp_str[:par_close].rfind('(')
            return funct(esp_str[:par_open] + str(funct(esp_str[par_open + 1:par_close])) \
                + (esp_str[par_close + 1:] if par_close != len(esp_str) else '')) 
        plus = esp_str.find('+')
        minus = esp_str.find('-')
        mult = esp_str.find('*') 
        div = esp_str.find('/')
        if (plus == -1) and (minus == -1) and (mult == -1) and (div == -1):
            return float(esp_str)
        if plus != -1:
            return funct(esp_str[:plus]) + funct(esp_str[plus + 1:])
        if minus != -1:
            return funct(esp_str[:minus]) - funct(esp_str[minus + 1:])
        if mult != -1:
            return funct(esp_str[:mult]) * funct(esp_str[mult + 1:])
        return float(funct(esp_str[:div]) / funct(esp_str[div + 1:]))
    await update.message.reply_text(f'{msg[1]} = {funct(msg[1])}')

async def weather(update: Update, context: CallbackContext):
    
    msg = update.message.text 
    items = msg.split()
    await update.message.reply_text(f'{func.weather(items[1])}')

async def download_yt(update: Update, context: CallbackContext):
    
    msg = update.message.text 
    items = msg.split()
    await update.message.reply_text(f'{dwl.download_yt(items[1])}')


