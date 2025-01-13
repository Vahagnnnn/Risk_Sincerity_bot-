from telebot import types

import telebot

bot = telebot.TeleBot('7574557958:AAHTGzsIT9_fYM-Ls54Z18pUg05RF1_e20Y')


def Show_Get_Choice(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Ռիսկ", callback_data="Get_Risk"))
    markup.add(types.InlineKeyboardButton("Անկեղծություն", callback_data="Get_Sincerity"))
    bot.send_message(message.chat.id, "Ռիսկ/Անկեղծություն", reply_markup=markup)


def Show_Get_Choice_Back(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Ռիսկ", callback_data="Get_Risk"))
    markup.add(types.InlineKeyboardButton("Անկեղծություն", callback_data="Get_Sincerity"))
    markup.add(types.InlineKeyboardButton("️⬅️վերադառնալ", callback_data="Back"))
    bot.edit_message_text("Ռիսկ/Անկեղծություն", message.chat.id, message.message_id, reply_markup=markup)
