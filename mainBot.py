import configuration
import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot(configuration.token)
userWish = None

@bot.message_handler(commands=['start'])
def message_start(message):
    userName = message.from_user.first_name
    userId = message.from_user.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info = types.KeyboardButton(text='/info')
    setWish = types.KeyboardButton(text='/setWish')
    getPlayer = types.KeyboardButton(text='/getPlayer')
    markup.add(info, setWish, getPlayer)
    bot.send_message(message.chat.id, f'Приветствую, <strong> {userName} !</strong>\n'
        f'Пожалуйста, пользуйтесь исключительно кнопками!\n\n'
            f'Команда чтобы узнать свое желание : <code> /info </code>\n'
            f'Команда чтобы записать свое желание : <code> /setWish </code>\n'
            f'Команда чтобы узнать кому дарить подарок и пожелание : <code> /setWish </code>\n'
        ,parse_mode="HTML", reply_markup=markup)

    connection = sqlite3.connect('santa.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (telegramId,userName,userWish) VALUES (?, ?, ?)', (userId, userName, ''))
    connection.commit()
    connection.close()

@bot.message_handler(commands=['setWish'])
def set_wish(message):
    bot.send_message(message.chat.id, f'Введите Ваше желание', parse_mode="HTML")
    bot.register_next_step_handler(message, us_wish)
def us_wish(message):
    global userWish
    userWish = message.text.strip()
    userId = message.from_user.id
    connection = sqlite3.connect('santa.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE Users SET userWish = ? WHERE telegramId = ?", (userWish, userId))
    print(userId, userWish)
    connection.commit()
    connection.close()
    bot.send_message(message.chat.id, f'Ваше пожелане записано!  - <code>{userWish}</code> !', parse_mode="HTML")


@bot.message_handler(commands=['info'])
def get_info(message):
    userId = message.from_user.id
    connection = sqlite3.connect('santa.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE telegramId = ?", (userId,))
    res = cursor.fetchall()
    if(userId == res[0][1]):
        userName = res[0][2]
        userWish = res[0][3]
    else:
        print('error penis get_info')
    connection.commit()
    connection.close()

    bot.send_message(message.chat.id,
        f'Приветствую, <strong>{userName} !</strong>\n'
        f'Ваше желание - <code>{userWish}</code> .', parse_mode="HTML")

@bot.message_handler(commands=['getPlayer'])
def get_player(message):

    usId = message.from_user.id

    connection = sqlite3.connect('santa.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE telegramId = ?", (usId,))
    res = cursor.fetchall()
    result_list = [list(row) for row in res]
    print(result_list)
    if (usId == res[0][1]):
        id = res[0][0]
        telegramId = res[0][1]
        userName = res[0][2]
        userWish = res[0][3]
        userPairs = res[0][4]
        cursor.execute("SELECT * FROM Users WHERE pair = ?", (id,))
        res2 = cursor.fetchall()
        playerName = res2[0][2]
        playerWish = res2[0][3]
        print(res2)
    else:
        print('error penis get_player')
        print(result_list)

    bot.send_message(message.chat.id,
                     f'Приветствую, <strong>{userName} !</strong>, Ваше желание {userWish}\n'
                     f'Ваш подопечный = <code>{playerName}</code>, его желание - {playerWish} .', parse_mode="HTML")


@bot.message_handler(content_types=['text'])
def use_text(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, пожалуйста, воспользутесь кнопками')


bot.infinity_polling()