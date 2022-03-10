# bot-button.py

import config
import mysql.connector
from mysql.connector import Error
import telebot
from telebot import types
from configDB import usH, usN, usP
from connectToDB import addValue

bot = telebot.TeleBot(config.token)
# import bot-token

def connectDB(hostN, userN, userP):
    global connection
# its really need
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostN,
            user = userN,
            passwd = userP)
        #print('Ok.')
    except Error as e:
        print(f'Error: {e}')

    return connection

global list
list=[]
connectDB(usH, usN, usP)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Загрузка в БД.")
    btn2 = types.KeyboardButton("Сброс значений.")
    #btn3 = types.KeyboardButton("Выгрузка из ДБ.")
    markup.add(btn1, btn2)
    global list
    list = []
# Two button to work with array.
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.first_name}. Значения передаются "
                          f"в каждом отдельном сообщении, где:"
f"""
1 - DATE
2 - MATCH
3 - TIP
4 - ODDS
5 - SCORE
6 - RESULT

Список сейчас пуст - {list}.
""", reply_markup=markup)
# start-message

@bot.message_handler(content_types=["text"])

def loadToDB(message):
    txt = message.text
    global list
    if (message.text == "Сброс значений."):
        list=[]
        bot.send_message(message.chat.id, text=f"List del: {list}.")
# That code clean array from data.
    elif (message.text == "Загрузка в БД."):

        bot.send_message(message.chat.id, text=f"Data: ")
# Show, what in DB.
# I need do it soon.
    elif (message.text == "Загрузка в БД."):
        bot.send_message(message.chat.id, text=f"Data {list} load.")

        addstr = f"""INSERT INTO `a0263496_bfb_stat_tgbot`.`TableTest` 
        (`date`,`match`,`tip`,`odds`,`score`,`result`)
        VALUES
        ('{list[0]}','{list[1]}','{list[2]}','{list[3]}','{list[4]}', '{list[5]}')"""
# Elements of array as values for SQL-request to DB.

        addValue(connection, addstr)
# Importing func to load values in table on DB
    elif len(list) < 5:
        if txt == "Начать запись." or txt == "Загрузка в БД."\
        or txt == "Сброс значений." or txt == "/start":
            pass
# Check, what data send by user.
        else:
            list.append(txt)
            bmes = bot.reply_to(message, f"Получено {txt}.\n{len(list)} - {list}.")
            bot.register_next_step_handler(bmes, loadToDB)
# Write 5 values to array.
    elif len(list) == 5:
        list.append(txt)
        bot.send_message(message.chat.id, text=f"Получено {list}.")
# Write last value and show all array.

bot.polling(none_stop=True)