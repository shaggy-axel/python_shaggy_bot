import time
import telebot

bot = telebot.TeleBot('1419052774:AAHz5KwK7aLBxnMS9GZJWEyOdUs-6-zvLpM')

name = bot.get_me()
@bot.message_handler(commands=['start'])
def send_text(message):
	t_time=time.ctime()
	t2_time=t_time[11]+t_time[12]
	if t2_time[0] == '0':
		t2_time = int(t2_time[1])
	else:
		t2_time = int(t2_time)

	if ((t2_time>=5) and (t2_time<=11)):
		bot.send_message(message.chat.id, 'Доброе утро!')
	if ((t2_time>=12) and (t2_time<=15)):
		bot.send_message(message.chat.id, 'Добрый день!')
	if ((t2_time>=16) and (t2_time<=21)):
		bot.send_message(message.chat.id, 'Добрый вечер!', name)
	if ((t2_time>=21) and (t2_time<=4)):
		bot.send_message(message.chat.id, 'Доброй ночи!')
# _____________________________________________________________
# Buttons

# 
# # def default_test(message):
# #     keyboard = types.InlineKeyboardMarkup()
# #     url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
# #     keyboard.add(url_button)
# #     bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


# @bot.message_handler(content_types=["text"])
# def buttons_bot(update,context):
# 	list_of_cities = ['Erode','Coimbatore','London', 'Thunder Bay', 'California']
# 	button_list = []
# 	for each in list_of_cities:
# 		button_list.append(InlineKeyboardButton(each, callback_data = each))
# 	reply_markup=InlineKeyboardMarkup(build_menu(button_list,n_cols=1)) #n_cols = 1 is for single column and mutliple rows
# 	bot.send_message(chat_id=update.message.chat_id, text='Choose from the following',reply_markup=reply_markup)
# def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
# 	menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
# 	if header_buttons:
# 		menu.insert(0, header_buttons)
# 	if footer_buttons:
# 		menu.append(footer_buttons)
# 	return menu



# _____________________________________________________________
# Run
bot.polling(none_stop=True)
