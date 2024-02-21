import telebot
import webbrowser
from telebot import types
import sqlite3

bot = telebot.TeleBot('6781510302:AAHnQ6AuIQ-cOVUg7H10OfkyWCc4jd02iBs')
conn = sqlite3.connect('db/boss.db', check_same_thread=False)
cursor = conn.cursor()
@bot.message_handler(commands=['start'])
def db_table_val(message):
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username

    file = open('../botbotbot/gachi.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('фитнес', callback_data='trainy_n')
    btn2 = types.InlineKeyboardButton('функциональный тренинг', callback_data='trainy_p')
    markup.row(btn1, btn2)
    markup.add()
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}. '
                                      f'На выбор даны два плана тренировок разного типа: '
                                      f'Фитнес-тренировки и функциональный тренинг',  reply_markup=markup)
    markup.add()
    resize_keyboard = True
    one_time_keyboard = True

@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    if call.data == 'trainy_n':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1🏋', callback_data='tn1')
        btn2 = types.InlineKeyboardButton('2🏋', callback_data='tn2')
        btn3 = types.InlineKeyboardButton('3☕', callback_data='tn3')
        btn4 = types.InlineKeyboardButton('4🏋', callback_data='tn4')
        btn5 = types.InlineKeyboardButton('5🏋', callback_data='tn5')
        btn6 = types.InlineKeyboardButton('6🏋', callback_data='tn6')
        btn7 = types.InlineKeyboardButton('7☕', callback_data='tn7')
        btn8 = types.InlineKeyboardButton('8🏋', callback_data='tn8')
        btn9 = types.InlineKeyboardButton('9🏋', callback_data='tn9')
        btn10 = types.InlineKeyboardButton('10☕', callback_data='tn10')
        btn11 = types.InlineKeyboardButton('11🏋', callback_data='tn11')
        btn12 = types.InlineKeyboardButton('12🏋', callback_data='tn12')
        btn13 = types.InlineKeyboardButton('13🏋', callback_data='tn13')
        btn14 = types.InlineKeyboardButton('14☕', callback_data='tn14')
        btn15 = types.InlineKeyboardButton('15🏋', callback_data='tn15')
        btn16 = types.InlineKeyboardButton('16🏋', callback_data='tn16')
        btn17 = types.InlineKeyboardButton('17🏋', callback_data='tn17')
        btn18 = types.InlineKeyboardButton('18🏋', callback_data='tn18')
        btn19 = types.InlineKeyboardButton('19🏋', callback_data='tn19')
        btn20 = types.InlineKeyboardButton('20🏋', callback_data='tn20')
        btn21 = types.InlineKeyboardButton('21🏋', callback_data='tn21')
        btn22 = types.InlineKeyboardButton('22🏋', callback_data='tn22')
        btn23 = types.InlineKeyboardButton('23🏋', callback_data='tn23')
        btn24 = types.InlineKeyboardButton('24🏋', callback_data='tn24')
        btn25 = types.InlineKeyboardButton('25🏋', callback_data='tn25')
        btn26 = types.InlineKeyboardButton('26🏋', callback_data='tn26')
        btn27 = types.InlineKeyboardButton('27🏋', callback_data='tn27')
        btn28 = types.InlineKeyboardButton('28🏋', callback_data='tn28')
        btn29 = types.InlineKeyboardButton('29🏋', callback_data='tn29')
        btn30 = types.InlineKeyboardButton('    ', callback_data='tn30')
        btn31 = types.InlineKeyboardButton('    ', callback_data='tn31')
        btn32 = types.InlineKeyboardButton('    ', callback_data='tn32')
        btn33 = types.InlineKeyboardButton('    ', callback_data='tn33')
        btn34 = types.InlineKeyboardButton('    ', callback_data='tn34')
        btn35 = types.InlineKeyboardButton('    ', callback_data='tn35')

            # создать ряды из кнопок
        markup.row(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        markup.row(btn8, btn9, btn10, btn11, btn12, btn13, btn14)
        markup.row(btn15, btn16, btn17, btn18, btn19, btn20, btn21)
        markup.row(btn22, btn23, btn24, btn25, btn26, btn27, btn28)
        markup.row(btn29, btn30, btn31, btn32, btn33, btn34, btn35)
        markup.add()

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Добро пожаловать! Тренировочная неделя для фитнеса           ', reply_markup = markup)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)

    elif call.data == 'trainy_p':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='tn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='tn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='tn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='tn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='tn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='tn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='tn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='tn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='tn9')
        btn10 = types.InlineKeyboardButton('10', callback_data='tn10')
        btn11 = types.InlineKeyboardButton('11', callback_data='tn11')
        btn12 = types.InlineKeyboardButton('12', callback_data='tn12')
        btn13 = types.InlineKeyboardButton('13', callback_data='tn13')
        btn14 = types.InlineKeyboardButton('14', callback_data='tn14')
        btn15 = types.InlineKeyboardButton('15', callback_data='tn15')
        btn16 = types.InlineKeyboardButton('16', callback_data='tn16')
        btn17 = types.InlineKeyboardButton('17', callback_data='tn17')
        btn18 = types.InlineKeyboardButton('18', callback_data='tn18')
        btn19 = types.InlineKeyboardButton('19', callback_data='tn19')
        btn20 = types.InlineKeyboardButton('20', callback_data='tn20')
        btn21 = types.InlineKeyboardButton('21', callback_data='tn21')
        btn22 = types.InlineKeyboardButton('22', callback_data='tn22')
        btn23 = types.InlineKeyboardButton('23', callback_data='tn23')
        btn24 = types.InlineKeyboardButton('24', callback_data='tn24')
        btn25 = types.InlineKeyboardButton('25', callback_data='tn25')
        btn26 = types.InlineKeyboardButton('26', callback_data='tn26')
        btn27 = types.InlineKeyboardButton('27', callback_data='tn27')
        btn28 = types.InlineKeyboardButton('28', callback_data='tn28')
        btn29 = types.InlineKeyboardButton('29', callback_data='tn29')
        btn30 = types.InlineKeyboardButton('    ', callback_data='tn30')
        btn31 = types.InlineKeyboardButton('    ', callback_data='tn31')
        btn32 = types.InlineKeyboardButton('    ', callback_data='tn32')
        btn33 = types.InlineKeyboardButton('    ', callback_data='tn33')
        btn34 = types.InlineKeyboardButton('    ', callback_data='tn34')
        btn35 = types.InlineKeyboardButton('    ', callback_data='tn35')

            # создать ряды из кнопок
        markup.row(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        markup.row(btn8, btn9, btn10, btn11, btn12, btn13, btn14)
        markup.row(btn15, btn16, btn17, btn18, btn19, btn20, btn21)
        markup.row(btn22, btn23, btn24, btn25, btn26, btn27, btn28)
        markup.row(btn29, btn30, btn31, btn32, btn33, btn34, btn35)
        markup.add()

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Тренировочная неделя для функционального тренинга', reply_markup=markup)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    elif call.data == 'tn20':
        next_menu2 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='вернуться в меню', callback_data='trainy_n')
        next_menu2.add(btn_1)
        res_1 = cursor.execute('SELECT work FROM february WHERE id = 21')
        work = res_1.fetchone()
        msg = work
        bot.send_message(call.message.chat.id, msg, reply_markup=next_menu2)

    elif call.data == 'tn21':
        next_menu2 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='вернуться в меню', callback_data='trainy_n')
        next_menu2.add(btn_1)
        res_1 = cursor.execute('SELECT work FROM february WHERE id = 22')
        work = res_1.fetchone()
        msg = work
        bot.send_message(call.message.chat.id, msg, reply_markup=next_menu2)

    elif call.data == 'tn23':
        next_menu2 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='вернуться в меню', callback_data='trainy_n')
        next_menu2.add(btn_1)
        res_1 = cursor.execute('SELECT work FROM february WHERE id = 23')
        work = res_1.fetchone()
        msg = work
        bot.send_message(call.message.chat.id, msg, reply_markup=next_menu2)

    elif call.data == 'tn24':
        next_menu2 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='вернуться в меню', callback_data='trainy_n')
        next_menu2.add(btn_1)
        res_1 = cursor.execute('SELECT work FROM february WHERE id = 24')
        work = res_1.fetchone()
        msg = work
        bot.send_message(call.message.chat.id, msg, reply_markup=next_menu2)

    elif call.data == 'tn25':
        next_menu2 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='вернуться в меню', callback_data='trainy_n')
        next_menu2.add(btn_1)
        res_1 = cursor.execute('SELECT work FROM february WHERE id = 25')
        work = res_1.fetchone()
        msg = work
        bot.send_message(call.message.chat.id, msg, reply_markup=next_menu2)

    elif call.data == 'tn26':
        next_menu2 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='вернуться в меню', callback_data='trainy_n')
        next_menu2.add(btn_1)
        res_1 = cursor.execute('SELECT work FROM february WHERE id = 26')
        work = res_1.fetchone()
        msg = work
        bot.send_message(call.message.chat.id, msg, reply_markup=next_menu2)

    elif call.data == 'tn27':
        next_menu2 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='вернуться в меню', callback_data='trainy_n')
        next_menu2.add(btn_1)
        res_1 = cursor.execute('SELECT work FROM february WHERE id = 27')
        work = res_1.fetchone()
        msg = work
        bot.send_message(call.message.chat.id, msg, reply_markup=next_menu2)
    elif call.data == 'tn28':
        next_menu2 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='вернуться в меню', callback_data='trainy_n')
        next_menu2.add(btn_1)
        res_1 = cursor.execute('SELECT work FROM february WHERE id = 28')
        work = res_1.fetchone()
        msg = work
        bot.send_message(call.message.chat.id, msg, reply_markup=next_menu2)
    elif call.data == 'tn29':
        next_menu2 = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='вернуться в меню', callback_data='trainy_n')
        next_menu2.add(btn_1)
        res_1 = cursor.execute('SELECT work FROM february WHERE id = 29')
        work = res_1.fetchone()
        msg = work
        bot.send_message(call.message.chat.id, msg, reply_markup=next_menu2)


#обработка любых данных, поступивших от пользователя
#должен быть внизу программы чтобы он не срабатывал первым и единственным
def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO user (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()

#def db_table_w(date: int, yummy: str):

    conn.commit()
#@bot.message_handler(content_types=['text'])
#def get_text_messages(message):
    #if message.text.lower() == 'привет':
        #bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!')
#чтобы бот работал постояннo
bot.polling(none_stop=True)
