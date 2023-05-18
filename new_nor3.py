import telebot
from telebot import types
import re
import random
import os
bot = telebot.TeleBot('5643211936:AAEYLgx-T4N0JpyPTZQ26oKvrO2iK48h_-s')
@bot.message_handler(commands=["start"])
def rey(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("ИМТ", url='https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D0%B4%D0%B5%D0%BA%D1%81_%D0%BC%D0%B0%D1%81%D1%81%D1%8B_%D1%82%D0%B5%D0%BB%D0%B0')
    markup.add(button1)
    bot.send_document(message.chat.id, open(r'1.html','rb'))
    bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEJBk9kZj94YFypzYQe1Ey4ZBmoXUGyawACwA0AArjWcUp5C0WFjY4Sti8E')
    try:
        file_1 = open('marks.txt', 'r').readlines()[1:]
        file_1 = [int(x) for x in file_1]
        arithmetic = str(round(sum(file_1) / len(file_1), 1))
        bot.send_message(message.chat.id,
                         f'Приветствую вас!\nЯ могу рассказать о вашей физической форме. Я - бот, который считает ваш индекс массы тела, дает полезные советы и любит цитаты. Мой рейтинг {arithmetic}',
                         reply_markup=markup)
    except ZeroDivisionError:
        bot.send_message(message.chat.id, 'Приветствую вас!\nЯ могу рассказать о вашей физической форме. Я - бот, который считает ваш индекс массы тела, дает полезные советы и любит цитаты. Мой рейтинг еще не сформирован',
                         reply_markup=markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Произвести расчет ИМТ")
    btn3 = types.KeyboardButton("/help")
    btn4 = types.KeyboardButton("поставить оценку")
    btn5 = types.KeyboardButton("посмотреть отзывы")
    btn6 = types.KeyboardButton("написать отзыв")
    btn7 = types.KeyboardButton("Обзор бота")
    markup.add(btn1, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id,'Воспользуйтесь моим функционалом, чтобы получить нужную вам информацию.',reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Произвести расчет ИМТ")
        button2 = types.KeyboardButton("Задать вопрос")
        button3 = types.KeyboardButton("/help")
        button4 = types.KeyboardButton("поставить оценку")
        button5 = types.KeyboardButton("посмотреть оценки")
        button6 = types.KeyboardButton("написать отзыв")
        button7 = types.KeyboardButton("Обзор бота")
        markup.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == 'поставить оценку'):
        bot.send_message(message.chat.id, 'Введите от одного до пяти')
        bot.register_next_step_handler(message, comment)
    elif (message.text == 'написать отзыв'):
        bot.send_message(message.chat.id, 'Введите свой отзыв')
        bot.register_next_step_handler(message, review)
    elif (message.text == 'посмотреть отзывы'):
        file_2 = open('review.txt', 'r').readlines()[1:]
        bot.send_message(message.chat.id, str("\n".join(file_2)))
    elif (message.text == 'Обзор бота'):
        bot.send_document(message.chat.id, open(r'1.html', 'rb'))
        bot.send_document(message.chat.id, 'Здесь вы всегда можете ознакомиться с функционалом бота и обратиться кдополнительным источникам информации')
    elif (message.text == '/help'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Функция Произвести расчет ИМТ")
        button2 = types.KeyboardButton("Функция Вернуться в главное меню")
        button3 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3)
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
def comment(message):
    if (message.text == '1') or (message.text == '2') or (message.text == '3') or (message.text == '4') or (
        message.text == '5'):
        file =  open('marks.txt', 'a').write('\n' + message.text)
        bot.send_message(message.chat.id, 'Ваша оценка записана')
    else:
        bot.send_message(message.chat.id, 'Выберите еще раз соотвествующую функцию поставить оценку и поставьте оценку еще раз. Введите оценку от одного до пяти')
def review(message):
    file = open('review.txt', 'a').write('\n' + message.text)
    bot.send_message(message.chat.id, 'Ваш отзыв записан')
def weightandheight(message):
    Citates = ["Если хочешь быть лучше других, будь готов делать то, что не хотят делать остальные",
     "Бог дал тело, на многое способное. Вам остается убедить в этом разум",
     "Если человек встал после падения, это не физика, а характер",
     "Важна не скорость продвижения. Важно, что продолжаешь идти», «Если не готов поработать, то приготовься к поражению»",
     "Победители играют, пока не добьются желаемого",
     "Спорт – не насилие. A положительные эмоции",
     "Если здоровье – символ свободы, то спорт – символ здоровья",
     "Некоторые вещи кажутся невозможными, пока сам не попробуешь выполнить",
     "Любая трудность дается для чего-то",
     "Если вы стремитесь к цели всем сердцем, то сумеете добиться своего, даже если другие считают это невозможным",
     "Возможность преодолеть себя —это, без сомнений, ценное свойство спорта",
     "Спорт – это лекарство от плохого настроения, от депрессий",
     "Вы должны наблюдать за вашим телом, если вы хотите, чтобы ваш ум работал правильно",
     "Надо непременно встряхивать себя физически, чтобы быть здоровым нравственно",
     "Настойчивость может превратить неудачу в выдающееся достижение",
     "Спорт – это труд, но не все с ним справляются",
     "Не бойся неудачи. Это путь к успеху ",
     "Никогда не говори «никогда», потому что ограничения, как и страхи, часто являются всего лишь иллюзией",
     "Спорт совершенствует физические качества и проверяет моральные",
     "Чем тяжелее битва, тем слаще победа",
     "Возраст не помеха. Это ограничение, которое вы накладываете на свой разум",
     "Способность побеждать самого себя, без сомнения, является самым ценным из всего, что дарит спорт",
     "Без напряженной работы над собой, без фанатизма ничего путного нельзя добиться ни в спорте, ни где-либо еще",
     "Не позволяйте тому, что вы не можете сделать, мешать тому, что вы можете сделать",
     "Независимо от обстоятельств, через которые вы можете пройти, просто преодолевайте их",
     "Можно мотивировать страхом, а можно мотивировать наградой. Но оба эти метода носят временный характер. Единственная постоянная вещь – это самомотивация",
     "Тот, кто хочет добиться убедительных побед, обязан пытаться прыгнуть выше головы",
     "У вас должна быть не только конкурентоспособность, но и способность, независимо от обстоятельств, с которыми вы сталкиваетесь, никогда не сдаваться",
     "Никогда не сдавайся! Неудача и отказ – только первый шаг к успеху",
     "Если ты будешь бояться, ты никогда не будешь радоваться жизни. У тебя есть только один шанс, так что ты должен повеселиться",
     "Беги, когда можешь, ходи, если нужно, ползай, если нужно; просто никогда не сдавайся",
     "Лучше начать и ошибаться, чем не начать и сожалеть всю жизнь",
     "Постоянные усилия, а не сила или интеллект, – это ключ к раскрытию нашего потенциала",
     "В жизни живет лучше тот, кто окреп хорошо физически",
     "Многие люди терпят неудачу только потому, что сдаются в двух шагах от успеха",
     "Бездействие порождает беспокойство и страх. Действие — уверенность и смелость. Если ты хочешь победить страх, не сиди дома и не думай об этом. Встань и действуй",
     "Начните оттуда, где вы сейчас находитесь. Используйте то, что у вас есть, и делайте всё, что можете",
     "Вы можете быть кем угодно, если вы уделите этому время"]
    try:
        weight, height = re.split(' и ', message.text, maxsplit=1)
        try:
            weight = float(weight)
            try:
                height = float(height)
                r = str(round(weight / (height * height)))
                message = bot.send_message(message.chat.id, 'Ваш ИМТ равен - ' + r)
                if (int(r)) in range(18, 26):
                    bot.send_message(message.chat.id, 'Ваш вес относится к категории "нормальный вес"')
                    bot.send_message(message.chat.id, random.choice(Citates))
                elif (int(r)) in range(26, 31):
                    bot.send_message(message.chat.id, 'Ваш вес относится к категории "изюыточный вес"')
                    bot.send_message(message.chat.id, random.choice(Citates))
                elif (int(r)) in range(31, 36):
                    bot.send_message(message.chat.id, 'Ваш вес относится к категории "ожирение первой степени"')
                    bot.send_message(message.chat.id, random.choice(Citates))
                else:
                    bot.send_message(message.chat.id, 'Ваш вес относится к категории "ожирение второй степени"')
                    bot.send_message(message.chat.id, random.choice(Citates))
            except Exception:
                bot.send_message(message.chat.id, 'Вы ввели данные не в правильном формате. Выберите еще раз подходящюю функцию и введите данные повторно.')
        except Exception:
            bot.send_message(message.chat.id, 'Вы ввели данные не в том формате. Выберите еще раз подходящюю функцию и введите данные повторно.')
    except Exception:
        bot.send_message(message.chat.id, 'Вы ввели данные не в том формате. Выберите еще раз подходящюю функцию и введите данные повторно.')
bot.polling(none_stop = True, interval = 0)