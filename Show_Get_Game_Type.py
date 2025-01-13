from telebot import types

import telebot

bot = telebot.TeleBot('7574557958:AAHTGzsIT9_fYM-Ls54Z18pUg05RF1_e20Y')


def Show_Get_Game_Type(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Անուններ", callback_data="Names"))
    markup.add(types.InlineKeyboardButton("Խաղ", callback_data="Show_Get_Choice_Back"))
    bot.send_message(message.chat.id, "Ընտրեք գործողություն", reply_markup=markup)


def Show_Get_Game_Type_Back(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Անուններ", callback_data="Names"))
    markup.add(types.InlineKeyboardButton("Խաղ", callback_data="Show_Get_Choice_Back"))
    bot.edit_message_text("Ընտրեք գործողություն", message.chat.id, message.message_id, reply_markup=markup)
