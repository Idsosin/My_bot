import telebot
from telebot import types

bot = telebot.TeleBot("6103807956:AAFdZQ-choNz1fB3qjHJcgKh-kLMCGCTfrk")

@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['интеграл', 'таблица', 'рк', 'таблица интегралов'])
def photo(message):
    photo = open('tab.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    start = types.KeyboardButton('/start')
    rk = types.KeyboardButton('/интеграл')
    help = types.KeyboardButton('/help')
    markup.add(start, rk, help)
    bot.send_message(message.chat.id, 'Выберите команду', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    m = message.text.lower()
    if m == 'таблица' or m == 'интеграл' or m == 'таблица интегралов' or m =='интегралы' or m == 'рк':
        photo = open('tab.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, крутое фото!')

bot.polling(none_stop=True)