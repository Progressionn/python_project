import telebot
from telebot import types
import re
bot = telebot.TeleBot('5643211936:AAEYLgx-T4N0JpyPTZQ26oKvrO2iK48h_-s')
@bot.message_handler(commands=["start"])
def rey(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("ИМТ", url='https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D0%B4%D0%B5%D0%BA%D1%81_%D0%BC%D0%B0%D1%81%D1%81%D1%8B_%D1%82%D0%B5%D0%BB%D0%B0')
    markup.add(button1)
    bot.send_message(message.chat.id, 'Приветствую вас!\nЯ могу рассказать о вашей физической форме. Я - бот, который считает ваш индекс массы тела, дает полезные советы и любит цитаты.', reply_markup=markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Произвести расчет ИМТ")
    btn2 = types.KeyboardButton("Задать вопрос")
    btn3 = types.KeyboardButton("/help")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,'Воспользуйтесь моим функционалом, чтобы получить нужную вам информацию.',reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if (message.text == 'Задать вопрос'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Цитаты")
            btn2 = types.KeyboardButton("Прочее")
            btn3 = types.KeyboardButton("Вернуться в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Здесь вы можете получить дополнительные подсказки', reply_markup=markup)
    elif (message.text == 'Цитаты'):
        markup = types.InlineKeyboardMarkup()
        button2 = types.InlineKeyboardButton("Цитаты", url='https://simpleslim.ru/50-luchshih-tsitat-pro-sport-i-zdorove/?ysclid=lfwflm44g1541471881')
        markup.add(button2)
        bot.send_message(message.chat.id, 'Здесь вы можете ознакомиться с другими цитатами', reply_markup=markup)
    elif (message.text == 'Прочее'):
        markup = types.InlineKeyboardMarkup()
        button3 = types.InlineKeyboardButton("Мифы об ИМТ", url='https://medaboutme.ru/articles/mify_ob_indekse_massy_tela_imt/?ysclid=lfwigwk8s9152935629')
        markup.add(button3)
        bot.send_message(message.chat.id, 'Здесь вы можете ознакомиться с другими фактами об ИМТ', reply_markup=markup)
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Произвести расчет ИМТ")
        button2 = types.KeyboardButton("Задать вопрос")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == '/help'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Функция Произвести расчет ИМТ")
        button2 = types.KeyboardButton("Функция Задать вопрос")
        button3 = types.KeyboardButton("Функция Цитаты")
        button4 = types.KeyboardButton("Функция Прочее")
        button5 = types.KeyboardButton("Функция Вернуться в главное меню")
        button6 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, "Здесь вы можете узнать о функционале данного телеграмм-бота.", reply_markup = markup)
    elif (message.text == 'Функция Произвести расчет ИМТ'):
        bot.send_message(message.chat.id, 'Эта функция запрашивает у пользователя его рост и вес и считает его индекс массы тела по следующей формуле - рост / (вес*вес) и округляет его до трех цифр после запятой.')
    elif (message.text == 'Функция Задать вопрос'):
        bot.send_message(message.chat.id, 'Этот бот только начинает разрабатываться, поэтому у функций потенциал реализован частично. Функция Задать вопрос предоставляет вам две дополнительные функции - Прочее и Цитаты, функционал которых вы также можете посмотреть, нажав соответствующую кнопку.')
    elif (message.text == 'Функция Цитаты'):
        bot.send_message(message.chat.id, 'Эта функция дает вам возможность перейти по ссылке и ознакомиться со списком цитат великих спортсменов. Эта функция также пока реализована не полностью и ее функционал будет расширяться.')
    elif (message.text == 'Функция Прочее'):
        bot.send_message(message.chat.id, 'Эта функция предоставляет вам возможность перейти по ссылке, где вы можете ознакомиться с дополнительной информацией про индекс массы тела.')
    elif (message.text == 'Функция Вернуться в главное меню'):
        bot.send_message(message.chat.id, 'Функция Вернуться в главное меню, возвращает пользователя в главное меню, где находятся две основные функции - Произвести расчет ИМТ и Задать вопрос, а также там вы можете обратиться за помощью с помощью функции /help')
    elif (message.text == 'Вернуться в главное меню'):
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.')
    elif (message.text == 'Произвести расчет ИМТ'):
        bot.send_message(message.chat.id,'Я очень рад, что вы согласились, произвести расчет ИМТ для вашего тела.\nДля того чтобы мне провести анализ, введите свой вес в килограммах и рост в метрах в формате {вес} и {рост}. Например 67 и 1.8')
        bot.register_next_step_handler(message, weightandheight)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("/help")
        button2 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Введите сообщение еще раз, соответствующее функционалу бота. Напишите /help, чтобы прочитать о функционале данного телеграмм-бота.')
def weightandheight(message):
    try:
        weight, height = re.split(' и ', message.text, maxsplit=1)
        try:
            weight = float(weight)
            bot.send_message(message.chat.id, 'Вы ввели данные корректно')
            try:
                height = float(height)
                r = str(round(weight / (height * height)))
                bot.send_message(message.chat.id, 'Ваш ИМТ равен ' + r)
            except Exception:
                bot.send_message(message.chat.id, 'Вы ввели данные не в правильном формате. Выберите еще раз подходящюю функцию и введите данные повторно.')
        except Exception:
            bot.send_message(message.chat.id, 'Вы ввели данные не в том формате. Выберите еще раз подходящюю функцию и введите данные повторно.')
    except Exception:
        bot.send_message(message.chat.id, 'Вы ввели данные не в том формате. Выберите еще раз подходящюю функцию и введите данные повторно.')
bot.polling(none_stop = True, interval = 0)
