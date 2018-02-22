from telegram.ext import Updater, CommandHandler
import telegram
import sqlite3
print('in the name of GOD')


updater = Updater('TOKEN')

user = {'name': None ,'family': None, 'student': None, 'phone':None}
conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users(name TEXT,family TEXT, student TEXT, phone TEXT)''')
conn.close()

def start_method(bot, update):
    global user
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, "in the name of GOD \n this bot is for take your information \n use \\name <first name> command to enter your first name \n use \\family <last name> command to enter your last name \n use \\student <student number> command to enter your student number \n use \\phone <phone number> command to enter your phone number" )

start_command = CommandHandler('start', start_method )
updater.dispatcher.add_handler(start_command)


def name_method(bot ,update, args):
    global user
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, 'i see .you send ' + str(args[0]))
    user['name']= args[0]
    name = user['name']

name_command = CommandHandler('name', name_method , pass_args = 1)
updater.dispatcher.add_handler(name_command)


def family_method(bot ,update, args):
    global user
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, 'i see .you send ' + str(args[0]))
    user['family']= args[0]
    family = user['family']

family_command = CommandHandler('family', family_method , pass_args = 1)
updater.dispatcher.add_handler(family_command)

def nu_d_method(bot ,update, args):
    global user
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, 'i see .you send ' + str(args[0]))
    user['student']= args[0]
    student = user['student']

nu_d_command = CommandHandler('student', nu_d_method , pass_args = 1)
updater.dispatcher.add_handler(nu_d_command)

def nu_tel_method(bot ,update, args):
    global user
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, 'i see .you send ' + str(args[0]))
    user['phone']= args[0]
    phone = user['phone']

nu_tel_command = CommandHandler('phone', nu_tel_method , pass_args = 1)
updater.dispatcher.add_handler(nu_tel_command)


def give_method(bot ,update):
    global user
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, user)
    print(user)

give_command = CommandHandler('g', give_method )
updater.dispatcher.add_handler(give_command)

if user != {'name': None ,'family': None, 'student': None, 'phone':None}:
    conn.commit()





updater.start_polling()
updater.idle()
