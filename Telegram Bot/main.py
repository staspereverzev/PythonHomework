from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *





app = ApplicationBuilder().token("5786521972:AAGTdVIhx6C5cWsmYIsxJEnRouXmlq6IZq4").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum",sum_command))
app.add_handler(CommandHandler("mult",mult_command))
app.add_handler(CommandHandler("div",div_command))
app.add_handler(CommandHandler("sub",sub_command))
app.add_handler(CommandHandler("calc",calc_command))
app.add_handler(CommandHandler("temp",weather))
app.add_handler(CommandHandler("dwl",download_yt))

print('server start')
app.run_polling()

