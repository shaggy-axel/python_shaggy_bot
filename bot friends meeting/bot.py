import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
 #    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	# button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
	# keyboard.add(button_geo)

 #    bot.send_message(message.chat.id, "Поделись местоположением", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель :heart:')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

# @bot.message_handler(content_types=['location'])
# def location(message):
#     if message.location is not None:
#         print(message.location)
#         print(message)


# @bot.message_handler(content_types=['sticker'])
# def send_sticker(message):
# 	if message.text.lower()=='люблю':
# 		bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALd7GAzJu518VQEikW3GDypAAEm91up4QACGQADwDZPE9BDgPYgVxRLHgQ')


bot.polling()
# 'file_id': 'CAACAgIAAxkBAAMvYDMbCWQ3YWd1hYruTDcvdoOJAkQAAh0AA5wlfD_WQsqHBh_Orx4E'
# 'file_id': 'CAACAgIAAxkBAANPYDMgOFTIMo1WVYHJrO3NlhnZreYAAh0AA5wlfD_WQsqHBh_Orx4E'

# 'file_id': 'AAMCAgADGQEAAy9gMxsJZDdhZ3WFiu5MNy92g4kCRAACHQADnCV8P9ZCyocGH86vxLEflC4AAwEAB20AAytgAAIeBA'