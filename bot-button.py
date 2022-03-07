# bot-button.py

import tokenbot
import telebot
from telebot import types
# import mysql-connector-python
# Пока что без SQL, сперва с кнопками надо разобраться.

bot = telebot.TeleBot(tokenbot.token)
# импорт токена бота

# cols = ('MATCH', 'TIP', 'ODDS', 'SCORE', 'RESULT')
# print(len(cols))    # 5
# print(cols[1])      # TIP

cols = ['MATCH', 'TIP', 'ODDS', 'SCORE', 'RESULT']
# print(len(cols))    # 5
# print(cols[3])      # SCORE
# lencols = len(cols)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать запись.")
    btn2 = types.KeyboardButton("Загрузка в БД.")
    btn3 = types.KeyboardButton("Сброс значений.")
    markup.add(btn1, btn2, btn3)
# три кнопки. Одна начинает запись, вторая отправляет данные в БД, третья - очищает введенные значения..
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.first_name}. Для передачи значений "
                          f"необходимо нажать на соответствующую кнопку и ввести поочередно, "
                          f"в каждом отдельном сообщении данные, где:"
f"""
1 - DATE 
2 - MATCH 
3 - TIP 
4 - ODDS 
5 - SCORE 
6 - RESULT                   
""", reply_markup=markup)



bot.polling(none_stop=True)