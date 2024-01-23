import telebot
import webbrowser
from telebot import types



bot = telebot.TeleBot('6781510302:AAHnQ6AuIQ-cOVUg7H10OfkyWCc4jd02iBs')


#Создать декоратор для создания ссылки на сайт
#@bot.message_handler(commands=['site', 'website'])
#Создать метод  с одним параметром
#def site(message):
    #webbrowser.open('https://www.youtube.com/')

#функция с инфой про пользователя, чат
#def main(message):
    #вывести обычный текст - приветствие - имя и фамилия,
    #можно найти в message если вывести его в bot.send_message(message.chat.id, message)
    #bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

def info(message):
    if message.text.lower() == 'Новобранец':
        bot.send_message(message.chat.id, 'Тренировочная неделя для новобранцев')

    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        #ответ на сообщение от пользователя
        bot.reply_to(message, f'ID: {message.from_user.id}')

####

@bot.message_handler(commands=['start'])
def t_n(message):
    # добавить картинку
    file = open('./gachi.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    markup = types.InlineKeyboardMarkup()
        # btn1 = types.InlineKeyboardButton('пн', callback.data = 'btn1web'
    btn1 = types.InlineKeyboardButton('новобранец', callback_data='trainy_n')
    btn2 = types.InlineKeyboardButton('продвинутый', callback_data='trainy_p')
            # создать ряды из кнопок
    markup.row(btn1, btn2)
    markup.add()
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}. '
                                      f'На выбор даны два плана тренировок разного уровня сложности. '
                                      f'Уровень "Новобранец" для начинающих, уровень "Продвинутый" для продолжающих.',  reply_markup=markup)
    markup.add()
    resize_keyboard = True
    one_time_keyboard = True

@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    if call.data == 'trainy_n':
            #bot.send_message(call.message.chat.id, 'Тренировочная неделя для новобранцев')
            #чтобы предыдущие сообщения убирались после нажатия кнопки
        markup = types.InlineKeyboardMarkup()
            # btn1 = types.InlineKeyboardButton('пн', callback.data = 'btn1web'
        btn1 = types.InlineKeyboardButton('пн', callback_data='tn1')
        btn2 = types.InlineKeyboardButton('вт', url='https://www.youtube.com/')
        btn3 = types.InlineKeyboardButton('ср', url='https://www.youtube.com/')
        btn4 = types.InlineKeyboardButton('чт', url='https://www.youtube.com/')
        btn5 = types.InlineKeyboardButton('пт', url='https://www.youtube.com/')
        btn6 = types.InlineKeyboardButton('сб', url='https://www.youtube.com/')
        btn7 = types.InlineKeyboardButton('вс', url='https://www.youtube.com/')
            # создать ряды из кнопок
        markup.row(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        markup.add()

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Тренировочная неделя для новобранцев', reply_markup = markup)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)

        @bot.callback_query_handler(func=lambda call: True)
        def tn(calltn):
            if calltn.data == 'tn1':
                bot.send_message(message.chat.id, 'тренировка понедельника', reply_markup=markup)
    elif call.data == 'trainy_p':
        markup2 = types.InlineKeyboardMarkup()
        # btn1 = types.InlineKeyboardButton('пн', callback.data = 'btn1web'
        bt1 = types.InlineKeyboardButton('пн', url='https://www.youtube.com/')
        bt2 = types.InlineKeyboardButton('вт', url='https://www.youtube.com/')
        bt3 = types.InlineKeyboardButton('ср', url='https://www.youtube.com/')
        bt4 = types.InlineKeyboardButton('чт', url='https://www.youtube.com/')
        bt5 = types.InlineKeyboardButton('пт', url='https://www.youtube.com/')
        bt6 = types.InlineKeyboardButton('сб', url='https://www.youtube.com/')
        bt7 = types.InlineKeyboardButton('вс', url='https://www.youtube.com/')
        # создать ряды из кнопок
        markup2.row(bt1, bt2, bt3, bt4, bt5, bt6, bt7)
        markup2.add()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = 'Тренировочная неделя для продвинутых', reply_markup=markup2)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)



    #обработка любых данных, поступивших от пользователя
#должен быть внизу программы чтобы он не срабатывал первыми единственным


    #bot.register_next_step_handler(message, on_click)
#функция будет работать сразу за предыдущей
#def on_click(message):
    #if message.text == 'Анкета':
        #bot.send_message(message.chat.id, 'Держи анкету')
    #if message.text == 'Новобранец':
        #bot.send_message(message.chat.id, 'Тренировочная неделя для новобранцев')
        #bot.register_next_step_handler(message, on_click)


    #elif message.text == 'Продвинутый':
        #bot.send_message(message.chat.id,'Тренировочная неделя для продвинутых')
    #one_time_keyboard = True
#@bot.message_handler(commands=['start', 'hello', 'main', 'train'])
#неделя для новобранцев

###






#чтобы бот работал постояннo
bot.polling(none_stop=True)
