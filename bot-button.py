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
    btn2 = types.KeyboardButton("Сброс")
    markup.add(btn1, btn2)
# Две кнопки. Одна начинает запись, вторая делает сброс.
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

cnt = 0

def enter(m):
    txt = m.text
    for cnt in range(len(cols)):
        brep = bot.reply_to(m, f'Значение передано: {txt}. '
                        f'Ждем ввода: {cols[cnt]}')
        cnt += 1
        bot.register_next_step_handler(brep, enter)
    else:
        bot.send_message(m.chat.id, text=f"Ввод завершен.")

@bot.message_handler(content_types=['text'])
def buttons(message):
    txt = message.text
    if (txt == "Начать запись."):
        bmes = bot.send_message(message.chat.id, text=f"Ввод DATE...")
        bot.register_next_step_handler(bmes, enter)
# При нажатии на кнопку выводится ссобщения о DATE
# и начинается ожидание ввода от пользователя с вызовом фунции ENTER.

    elif (txt == "Сброс"):
        bot.send_message(message.chat.id, text=f"Txt me something.")
# Тут будет отмена ввода.

bot.polling(none_stop=True)