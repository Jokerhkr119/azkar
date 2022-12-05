import requests
import telebot
from telebot import types, TeleBot
import random

bot = telebot.TeleBot('5933344936:AAFqaKRaB0nPuq9UBKaoE5dB38HvHbqpSyQ')

az_btn = types.InlineKeyboardButton(text='- اذكار 🍃',callback_data='az_btn')
key = requests.get(f'https://nodz.club/API/athkar.php').json()['Rick']
@bot.message_handler(commands=['start'])
def Welcome(message):
	FIRST_NAME = message.from_user.first_name
	
	b = types.InlineKeyboardMarkup()
	b.row_width = 1
	b.add(az_btn)
	bot.reply_to(message,f'❤️ ⌯ أهلا ← {FIRST_NAME} في بوت الاذكار ,\n\n 🍃 ⌯ أرسل /az او أذكار او يمكنك الضغط على الزر ادناه لارسال أذكار ♥️٫\n---------', reply_markup=b)
@bot.message_handler(commands=['az'])
def az_cmd(message):
	bot.reply_to(message,key)
@bot.message_handler(func=lambda m:True)
def Az(message):
	
	msg = message.text
	if msg=='اذكار':
		
		bot.send_message(message.chat.id,key)

@bot.callback_query_handler(func=lambda call:True)
def azbtn(call):
	if call.data=='az_btn':
		
		bot.send_message(call.message.chat.id,key)
		
bot.infinity_polling()
