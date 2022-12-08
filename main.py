from config import token
import telebot
from telebot import types

bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['get_info', 'start'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Yes', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='No', callback_data='no')

    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'Do you want to know information about yourself?',
                     reply_markup=markup_inline
    )

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_id = types.KeyboardButton('My ID')
        item_name = types.KeyboardButton('My Name')
        item_geo = types.KeyboardButton('My Location', request_location=True)
        item_us_name = types.KeyboardButton('My UserName')
        item_phone = types.KeyboardButton('My Phone')
        markup_reply.add(item_id, item_name, item_geo, item_us_name, item_phone,)
        bot.send_message(call.message.chat.id,'Push button👇',
                         reply_markup=markup_reply
        )
    elif call.data == 'no':
        pass
@bot.message_handler(content_types=['text', 'contact'])
def get_text(message):
    if message.text == 'My ID':
        bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
    if message.text == 'My Name':
        bot.send_message(message.chat.id, f'Your Name: {message.from_user.first_name}{message.from_user.last_name}')
    if message.text == 'My Location':
        bot.send_message(message.chat.id, f'Your location: {message.from_user.location}')
    if message.text == 'My UserName':
        bot.send_message(message.chat.id, f'Your UserName: {message.from_user.username}')
    if message.text == 'My Phone':
        bot.send_message(message.chat.id, f'Your PhoneNumber: {message.contact.phone_number}')

bot.polling(none_stop=True, interval=0)
