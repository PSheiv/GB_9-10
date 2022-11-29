import random
import telebot
from telebot import types
token = ""
bot = telebot.TeleBot(token)

markup = types.ReplyKeyboardMarkup()
itembtn1 = types.KeyboardButton('Калькулятор')
itembtn2 = types.KeyboardButton('Угадай Число')
itembtn3 = types.KeyboardButton('Техподдержка')
itembtn4 = types.KeyboardButton('Основное меню')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4)


def getRndNum():
    return random.randint(1, 101)
rndNum = getRndNum()

# начальный счетчик для подсчета попыток угадывания случайного числа
countTries = 0

# записываю текущее состояние
def setCurrentState(state):
    with open("currentstate.txt", "w", encoding="utf-8") as f:
        print(state)
        f.write(str(state))


# первое обращение к боту
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, для работы воспользуйся клавиатурой", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def hello_user(message):
    if 'Основное меню' in message.text:
        bot.reply_to(message, 'Вы в основном меню')
        setCurrentState(0)

    elif message.text == 'Калькулятор':
        bot.reply_to(message, 'Игра в калькулятор. Введите выражение')
        setCurrentState(1)

    elif message.text == 'Угадай Число':
        bot.reply_to(
            message, 'Игра в число, я загадал его, введи от 1 до 100 и начни угадывать')
        setCurrentState(2)

    elif message.text == 'Техподдержка':
        bot.reply_to(message, 'Давай передадим сообщение техподдержке')
        setCurrentState(3)
    else:
        with open("currentstate.txt", "r", encoding="utf-8") as f:
            currentState = f.read()

        print(currentState, type(currentState), len(currentState))

        if currentState == "1":
            print(message.text)
            bot.reply_to(message, f'ответ = {eval(message.text)}')

        elif currentState == "2":
            global rndNum
            global countTries
            if int(message.text) != rndNum:
                bot.reply_to(
                    message, f'ответ = {rndNum}, а ты прислал {message.text}')
                countTries = countTries + 1
            else:
                bot.reply_to(
                    message, f'ответ = {rndNum}, ура, ты победил за {countTries} раз')

                rndNum = getRndNum()
                countTries = 0

        elif currentState == "3":
            userLog = f'{str(message.from_user.id)}/{str(message.from_user.first_name)}/{str(message.from_user.username)}/{str(message.text)}'

            with open("support.txt", "a+", encoding="utf-8") as f:
                f.write(str(userLog))
                f.write('\n')

            bot.reply_to(message, "Ваше обращение передано")

        elif currentState == "0":
            bot.reply_to(
                message, f'Вы в основном меню и только что послали следующее сообщение: {eval(message.text)}')

        else:
            bot.reply_to(message, 'что-то пошло не так, обратитесь в техподдержку')

bot.infinity_polling()
