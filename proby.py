#обычные кнопки выбора уровня
#@bot.message_handler(commands=['start'])

#def start(message):
    #markup = types.ReplyKeyboardMarkup()
    #s = types.KeyboardButton('start')
    #markup = types.ReplyKeyboardMarkup()
    #A0 = types.KeyboardButton('Анкета')
    #A1 = types.KeyboardButton('Новобранец')
    #A2 = types.KeyboardButton('Продвинутый')
    #resize_keyboard = True
    #one_time_keyboard = True
    #markup.row(A1, A2)

    #bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}. '
                                      #f'На выбор даны два плана тренировок разного уровня сложности. '
                                      #f'Уровень "Новобранец" для начинающих, уровень "Продвинутый" для всех остальных.', reply_markup=markup)
    #добавить картинку
    #file = open('./gachi.jpg', 'rb')
    #bot.send_photo(message.chat.id, file, reply_markup=markup)

#@bot.message_handler(commands=['train_n'])
#def train_n(message):
    #markup = types.InlineKeyboardMarkup()
        # btn1 = types.InlineKeyboardButton('пн', callback.data = 'btn1web'
    #btn1 = types.InlineKeyboardButton('пн', url='https://www.youtube.com/')
    #btn2 = types.InlineKeyboardButton('вт', url='https://www.youtube.com/')
    #btn3 = types.InlineKeyboardButton('ср', url='https://www.youtube.com/')
    #btn4 = types.InlineKeyboardButton('чт', url='https://www.youtube.com/')
    #btn5 = types.InlineKeyboardButton('пт', url='https://www.youtube.com/')
    #btn6 = types.InlineKeyboardButton('сб', url='https://www.youtube.com/')
    #btn7 = types.InlineKeyboardButton('вс', url='https://www.youtube.com/')
        # создать ряды из кнопок
    #markup.row(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    #markup.add()
    #bot.send_message(message.chat.id, 'январь 2024 для новобранцев', reply_markup=markup)
    #markup.add()

#@bot.message_handler(commands=['train_p'])
#def train_p(message):
    #markup2 = types.InlineKeyboardMarkup()
        # btn1 = types.InlineKeyboardButton('пн', callback.data = 'btn1web'
    #bt1 = types.InlineKeyboardButton('пн', url='https://www.youtube.com/')
    #bt2 = types.InlineKeyboardButton('вт', url='https://www.youtube.com/')
    #bt3 = types.InlineKeyboardButton('ср', url='https://www.youtube.com/')
    #bt4 = types.InlineKeyboardButton('чт', url='https://www.youtube.com/')
    #bt5 = types.InlineKeyboardButton('пт', url='https://www.youtube.com/')
    #bt6 = types.InlineKeyboardButton('сб', url='https://www.youtube.com/')
    #bt7 = types.InlineKeyboardButton('вс', url='https://www.youtube.com/')
        # создать ряды из кнопок
    #markup2.row(bt1, bt2, bt3, bt4, bt5, bt6, bt7)
    #markup2.add()
#обработка callback_data
#@bot.callback_query_handler(func=lambda callback: True)
#def callback_message(callback)
    #if callback.data = 'btn1web':

    #resize_keyboard = True
    #bot.send_message(message.chat.id, 'январь 2024 для продвинутых', reply_markup=markup)
    #markup.add()


