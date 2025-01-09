from pygame.examples.midi import NullKey
from telebot import types
import telebot
import sqlite3
import telebot

bot = telebot.TeleBot('7574557958:AAHTGzsIT9_fYM-Ls54Z18pUg05RF1_e20Y')


def names(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Նայել մասնակիցների անունները", callback_data="View_All_Names"))
    # markup.add(types.InlineKeyboardButton("Ջնջել անուն", callback_data="Delete_Name"))
    markup.add(types.InlineKeyboardButton("Գրանցել մասնակիցների անունները", callback_data="Add_Name"))
    markup.add(types.InlineKeyboardButton("⬅️Վերադառնալ", callback_data="Back"))
    bot.edit_message_text("Ընտրեք գործողություն", message.chat.id, message.message_id, reply_markup=markup)


def View_All_Names(message):
    conn = sqlite3.connect('../Risk_Sincerity.db')
    cursor = conn.cursor()
    chat_id = message.chat.id

    cursor.execute("SELECT Names FROM Names WHERE ChatID = ?", (chat_id,))
    names = cursor.fetchall()
    cursor.close()
    conn.close()




    if names:
        names_str = names[0][0]
        names = [name.strip() for name in names_str.split(',')]
        numbered_names = [f"{i + 1}) {name}" for i, name in enumerate(names)]

        formatted_message = '\n'.join(numbered_names)
        bot.send_message(message.chat.id, f"Մասնակիցներ📄\n{formatted_message}")
    else:
        bot.send_message(message.chat.id, "Ցուցակը դատարկ է📄")