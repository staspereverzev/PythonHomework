# from isOdd import isOdd

# print(isOdd(1)) 
# print(isOdd(4)) 

# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     # Do some work
#     bar.next()
# bar.finish()

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

# import matplotlib.pyplot as plt
# import numpy as np

# plt.style.use('_mpl-gallery')

# # make data
# np.random.seed(1)
# x = np.linspace(0, 8, 16)
# y1 = 3 + 4*x/8 + np.random.uniform(0.0, 0.5, len(x))
# y2 = 1 + 2*x/8 + np.random.uniform(0.0, 0.5, len(x))

# # plot
# fig, ax = plt.subplots()

# ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
# ax.plot(x, (y1 + y2)/2, linewidth=2)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()

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


print('server start')
app.run_polling()