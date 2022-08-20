import telebot
from telebot import types

bot = telebot.TeleBot("5776525243:AAG8t7rkza924VXR0rOh6xNvIcnGiCa8iOM")

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, 'Привет, выбери нужный знак зодиака', parse_mode= "html")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    website = types.KeyboardButton('Телец')
    start = types.KeyboardButton('Лев')
    markup.add(website,start)
    bot.send_message(message.chat.id,  reply_markup=markup)





# @bot.message_handler(commands=['text'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
#     website = types.KeyboardButton('Телец')
#     start = types.KeyboardButton('Лев')
#     markup.add(website,start)
#     bot.send_message(message.chat.id, 'Выберите нужный знак зодиака', reply_markup=markup)



bot.polling(none_stop=True)



