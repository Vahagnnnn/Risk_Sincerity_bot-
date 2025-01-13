import telebot
from telebot import types
import random
import sqlite3
import Show_Get_Choice
import Show_Get_Game_Type
import Names
from Tables import tables
from SetData import start_handler

bot = telebot.TeleBot('7574557958:AAHTGzsIT9_fYM-Ls54Z18pUg05RF1_e20Y')


@bot.message_handler(commands=['start'])
def start(message):
    start_handler(message)
    tables()
    welcome_message = f"""
Բարև սիրելի {message.from_user.first_name} 😊
սա տելեգրամ բոտ է որը տրամադրում է 
հարցրեր կամ առաջադրանքներ
Ռիսկի և Անկեղծություն խաղի համար
-----------------------------------------------------------------------
Հրամանների ցուցակ
/play - Սկսել խաղը
/add - Ավելացնել հարցրեր և առաջադրանքներ
/contact - Տելեգրամ
/help - Օգնություն
"""
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Admin Instagram", url="https://www.instagram.com/___vahagn/"))
    # bot.send_message(message.chat.id, "Մեր կայքը", reply_markup=markup)
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)


@bot.message_handler(commands=['play'])
def play(message):
    start_handler(message)
    reply_markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "😊")
    Show_Get_Game_Type.Show_Get_Game_Type(message)


@bot.message_handler(commands=['add'])
def add(message):
    bot.send_message(message.chat.id, "Գրիր ադմինի գաղտնաբառ")
    bot.register_next_step_handler(message, Check_password)


@bot.message_handler(commands=['contact'])
def contact(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Telegram", url="https://t.me/Vahagnnnn"))
    markup.add(types.InlineKeyboardButton("Instagram", url="https://www.instagram.com/___vahagn/"))
    bot.send_message(message.chat.id, "Առաջարկների համար կարող եք գրել📩", reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    welcome_message = f"""
    Հրամանների ցուցակ
/play - Սկսել խաղը
/add - Ավելացնել հարցրեր և առաջադրանքներ
/contact - Տելեգռամ
/help - Օգնություն
        """
    hide_markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, welcome_message, reply_markup=hide_markup)


def Show_Add(message):
    # markup = types.InlineKeyboardMarkup()
    # markup.row(types.InlineKeyboardButton("Ավելացնել Ռիսկ", callback_data="Set_Risk"),
    #            types.InlineKeyboardButton("Ավելացնել Անկեղծություն", callback_data="Set_Sincerity"))
    # markup.row(types.InlineKeyboardButton("Նայել ռիսկերը", callback_data="View_All_Risk"),
    #            types.InlineKeyboardButton("Նայել անկեղծությունները", callback_data="View_All_Sincerity"))
    # markup.row(types.InlineKeyboardButton("Ջնջել ռիսկ ցուցակից", callback_data="Delete_Risk_Input_ID"),
    #            types.InlineKeyboardButton("Ջնջել անկեղծությունները ցուցակից",
    #                                       callback_data="Delete_Sincerity_Input_ID"))

    reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    reply_markup.row(types.KeyboardButton("Ավելացնել Ռիսկ"),
                     types.KeyboardButton("Ավելացնել Անկեղծություն"))
    reply_markup.row(types.KeyboardButton("Նայել ռիսկերը"),
                     types.KeyboardButton("Նայել անկեղծությունները"))
    reply_markup.row(types.KeyboardButton("Ջնջել ռիսկ ցուցակից"),
                     types.KeyboardButton("Ջնջել անկեղծությունները ցուցակից"))

    bot.send_message(message.chat.id, "Ռիսկ/Անկեղծություն", reply_markup=reply_markup)
    bot.register_next_step_handler(message, on_Click)


def on_Click(message):
    if message.text == "Ավելացնել Ռիսկ":
        bot.send_message(message.chat.id, "Ներմուծիր առաջադրանք Ռիսկի համար")
        bot.register_next_step_handler(message, Set_Risk)
    elif message.text == "Ավելացնել Անկեղծություն":
        bot.send_message(message.chat.id, "Ներմուծիր հարց անկեղծության համար")
        bot.register_next_step_handler(message, Set_Sincerity)
    elif message.text == "Նայել ռիսկերը":
        View_All_Risk(message)
        bot.register_next_step_handler(message, on_Click)
    elif message.text == "Նայել անկեղծությունները":
        View_All_Sincerity(message)
        bot.register_next_step_handler(message, on_Click)
    elif message.text == "Ջնջել ռիսկ ցուցակից":
        Delete_Risk_Input_ID(message)
    elif message.text == "Ջնջել անկեղծությունները ցուցակից":
        Delete_Sincerity_Input_ID(message)
    elif message.text == "/play":
        play(message)
    elif message.text == "/help":
        help(message)
    elif message.text == "/contact":
        contact(message)
    elif message.text == "/start":
        start(message)


# def Show_Get_Choice(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Ռիսկ", callback_data="Get_Risk"))
#     markup.add(types.InlineKeyboardButton("Անկեղծություն", callback_data="Get_Sincerity"))
#     bot.send_message(message.chat.id, "Ռիսկ/Անկեղծություն", reply_markup=markup)


def Check_password(message):
    if message.text.strip() == "pix":
        Show_Add(message)
    else:
        bot.send_message(message.chat.id, "Սխալ գաղտնաբառ")
        help(message)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "Get_Risk":
        Get_Risk(callback.message)
    elif callback.data == "Get_Sincerity":
        Get_Sincerity(callback.message)
    elif callback.data == "Show_Get_Choice_Back":
        Show_Get_Choice.Show_Get_Choice_Back(callback.message)
    elif callback.data == "Names":
        Names.names(callback.message)
    elif callback.data == "View_All_Names":
        Names.View_All_Names(callback.message)
    elif callback.data == "Add_Name":
        add_name(callback.message)
    elif callback.data == "Back":
        Show_Get_Game_Type.Show_Get_Game_Type_Back(callback.message)
    # elif callback.data == "Delete_Name":
    #     delete_name(callback.message)
    # elif callback.data == "Set_Risk":
    #     bot.send_message(callback.message.chat.id, "Ներմուծիր առաջադրանք Ռիսկի համար")
    #     bot.register_next_step_handler(callback.message, Set_Risk)
    # elif callback.data == "Set_Sincerity":
    #     bot.send_message(callback.message.chat.id, "Ներմուծիր հարց անկեղծության համար")
    #     bot.register_next_step_handler(callback.message, Set_Sincerity)
    # elif callback.data == "View_All_Risk":
    #     View_All_Risk(callback.message)
    # elif callback.data == "View_All_Sincerity":
    #     View_All_Sincerity(callback.message)
    # elif callback.data == "Delete_Risk_Input_ID":
    #     Delete_Risk_Input_ID(callback.message)
    # elif callback.data == "Delete_Sincerity_Input_ID":
    #     Delete_Sincerity_Input_ID(callback.message)


def Get_Risk(message):
    conn = sqlite3.connect('Risk_Sincerity.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Risk")
    lastID = cursor.fetchone()[0]
    randoId = random.randint(1, lastID)
    cursor.execute(f'SELECT * FROM Risk WHERE ID=={randoId}')
    RiskItems = cursor.fetchone()
    Risks = RiskItems[1]

    chat_id = message.chat.id
    cursor.execute("SELECT Names FROM Names WHERE ChatID = ?", (chat_id,))
    names = cursor.fetchall()
    cursor.close()
    conn.close()
    if names:
        names_str = names[0][0]
        names = [name.strip() for name in names_str.split(',')]
        random_name = random.choice(names)
        bot.send_message(message.chat.id, f"<pre>{random_name}</pre>\n" + Risks, parse_mode='HTML')
        Show_Get_Choice.Show_Get_Choice(message)
    else:
        bot.send_message(message.chat.id, "<pre>Ռիսկ</pre>\n" + Risks, parse_mode='HTML')
        Show_Get_Choice.Show_Get_Choice(message)

def Set_Risk(message):
    RiskText = message.text.strip()
    conn = sqlite3.connect('Risk_Sincerity.db')
    cursor = conn.cursor()

    cursor.execute(f'INSERT INTO Risk(Tasks) VALUES("{RiskText}")')
    conn.commit()

    cursor.execute("SELECT ID, Tasks FROM Risk ORDER BY ID")
    rows = cursor.fetchall()

    id_mapping = {old_id: new_id for new_id, (old_id, _) in enumerate(rows, start=1)}

    for old_id, new_id in id_mapping.items():
        cursor.execute("UPDATE Risk SET ID = ? WHERE ID = ?", (new_id, old_id))
    conn.commit()

    cursor.close()
    conn.close()

    bot.send_message(message.chat.id, "Ներմուծումը հաջողվեց✅")
    Show_Add(message)
    View_All_Risk(message)


def View_All_Risk(message):
    conn = sqlite3.connect('Risk_Sincerity.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Risk')
    RiskItems = cursor.fetchall()
    Risks = ""
    for i in RiskItems:
        Risks += f"{i}\n"
    cursor.close()
    conn.close()
    bot.send_message(message.chat.id, "Ռիսկերի Ցուցակ📄")

    max_length = 4096
    message_content = Risks

    while len(message_content) > max_length:
        bot.send_message(message.chat.id, message_content[:max_length])
        message_content = message_content[max_length:]
    bot.send_message(message.chat.id, message_content)


def Delete_Risk_Input_ID(message):
    bot.send_message(message.chat.id, "Ներմուծեք 🆔")
    bot.register_next_step_handler(message, Delete_Risk)


def Delete_Risk(message):
    Erasable_Risk_Id = message.text.strip()
    conn = sqlite3.connect('Risk_Sincerity.db')
    cursor = conn.cursor()

    cursor.execute(f'DELETE FROM Risk WHERE ID == {Erasable_Risk_Id}')
    conn.commit()

    cursor.execute("SELECT ID, Tasks FROM Risk ORDER BY ID")
    rows = cursor.fetchall()

    id_mapping = {old_id: new_id for new_id, (old_id, _) in enumerate(rows, start=1)}

    for old_id, new_id in id_mapping.items():
        cursor.execute("UPDATE Risk SET ID = ? WHERE ID = ?", (new_id, old_id))
    conn.commit()
    cursor.close()
    conn.close()
    View_All_Risk(message)
    bot.register_next_step_handler(message, on_Click)


def Get_Sincerity(message):
    conn = sqlite3.connect('Risk_Sincerity.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Sincerity")
    lastID = cursor.fetchone()[0]
    randoId = random.randint(1, lastID)
    cursor.execute(f'SELECT * FROM Sincerity WHERE ID=={randoId}')
    SincerityItems = cursor.fetchone()
    Sincerities = SincerityItems[1]

    chat_id = message.chat.id
    cursor.execute("SELECT Names FROM Names WHERE ChatID = ?", (chat_id,))
    names = cursor.fetchall()
    cursor.close()
    conn.close()

    if names:
        names_str = names[0][0]
        names = [name.strip() for name in names_str.split(',')]
        random_name = random.choice(names)

        bot.send_message(message.chat.id, f"<pre>{random_name}</pre>\n" + Sincerities, parse_mode='HTML')
        Show_Get_Choice.Show_Get_Choice(message)
    else:
        bot.send_message(message.chat.id, "<pre>Անկեղծություն</pre>\n" + Sincerities, parse_mode='HTML')
        Show_Get_Choice.Show_Get_Choice(message)


def Set_Sincerity(message):
    SincerityText = message.text.strip()
    conn = sqlite3.connect('Risk_Sincerity.db')
    cursor = conn.cursor()

    cursor.execute(f'INSERT INTO Sincerity(Questions) VALUES("{SincerityText}")')
    conn.commit()

    cursor.execute("SELECT ID, Questions FROM Sincerity ORDER BY ID")
    rows = cursor.fetchall()

    id_mapping = {old_id: new_id for new_id, (old_id, _) in enumerate(rows, start=1)}

    for old_id, new_id in id_mapping.items():
        cursor.execute("UPDATE Sincerity SET ID = ? WHERE ID = ?", (new_id, old_id))
    conn.commit()

    cursor.close()
    conn.close()

    bot.send_message(message.chat.id, "Ներմուծումը հաջողվեց✅")
    Show_Add(message)
    View_All_Sincerity(message)


def View_All_Sincerity(message):
    conn = sqlite3.connect('Risk_Sincerity.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Sincerity')
    SincerityItems = cursor.fetchall()
    Sincerities = ""
    for i in SincerityItems:
        Sincerities += f"{i}\n"
    cursor.close()
    conn.close()
    bot.send_message(message.chat.id, "Անկեղծությունների Ցուցակ📄")

    max_length = 4096
    message_content = Sincerities

    while len(message_content) > max_length:
        bot.send_message(message.chat.id, message_content[:max_length])
        message_content = message_content[max_length:]
    bot.send_message(message.chat.id, message_content)


def Delete_Sincerity_Input_ID(message):
    bot.send_message(message.chat.id, "Ներմուծեք 🆔")
    bot.register_next_step_handler(message, Delete_Sincerity)


def Delete_Sincerity(message):
    Erasable_Sincerity_Id = message.text.strip()
    conn = sqlite3.connect('Risk_Sincerity.db')
    cursor = conn.cursor()

    cursor.execute(f'DELETE FROM Sincerity WHERE ID == {Erasable_Sincerity_Id}')
    conn.commit()

    cursor.execute("SELECT ID, Questions FROM Sincerity ORDER BY ID")
    rows = cursor.fetchall()

    id_mapping = {old_id: new_id for new_id, (old_id, _) in enumerate(rows, start=1)}

    for old_id, new_id in id_mapping.items():
        cursor.execute("UPDATE Sincerity SET ID = ? WHERE ID = ?", (new_id, old_id))
    conn.commit()

    cursor.close()
    conn.close()
    View_All_Sincerity(message)
    bot.register_next_step_handler(message, on_Click)


# --------Names--------------------------------------------------------------------

def add_name(message):
    bot.send_message(message.chat.id, "Ներմուծեք խաղացողների անունները բաժանված ստորակետներով"
                                      "(Այն անունները որոնք կրկնվում են ներմուծեք ազագնուններով)")
    bot.register_next_step_handler(message,insert_names)

def insert_names(message):
    conn = sqlite3.connect('Risk_Sincerity.db')
    cursor = conn.cursor()

    chat_id = message.chat.id


# --------EMPTY TABLE--------------------------------------------------------------------

    cursor.execute('''
        DELETE FROM Names
        WHERE ChatID = ?
    ''', (chat_id,))
    conn.commit()

# --------/EMPTY TABLE/--------------------------------------------------------------------

# --------Names--------------------------------------------------------------------

    text = message.text.strip().split(',')
    names = [name.strip() for name in text if name.strip()]

    if len(names) <2:
        if text=='/play':
            play(message)
        else:
            bot.send_message(message.chat.id, "Խնդրում եմ մուտքագրեք գոնե երկու անուն, բաժանված ստորակետներով")
            bot.register_next_step_handler(message,insert_names)
    else:
        names_str = ", ".join(names)
        numbered_names = [f"{i + 1}) {name}" for i, name in enumerate(names)]
        cursor.execute('''
            INSERT INTO Names (ChatID, Names)
            VALUES (?, ?)
        ''', (chat_id, names_str))

        conn.commit()
        # bot.send_message(message.chat.id, f"Անունները հաջողությամբ ավելացվել են \n{str('\n'.join(numbered_names))}")
        bot.send_message(message.chat.id, f"Անունները հաջողությամբ ավելացվել են \n" + '\n'.join(numbered_names))
        # bot.send_message(message.chat.id, f"Անունները հաջողությամբ ավելացվել են \\n{'\\n'.join(numbered_names)}")
    conn.close()
# --------/Names/--------------------------------------------------------------------
# --------Delete Name--------------------------------------------------------------------

# def delete_name(message):
#     conn = sqlite3.connect('../Risk_Sincerity.db')
#     cursor = conn.cursor()
#
#     chat_id = message.chat.id
#
#     cursor.execute('''
#             DELETE FROM Names
#             WHERE ChatID = ?
#         ''', (chat_id,))
#     conn.commit()

# --------/Delete Name/--------------------------------------------------------------------

# while True:
#     try:
#         bot.polling(none_stop=True, interval=0, timeout=20)
#     except Exception as e:
#         print(f"Connection error: {e}")
#         time.sleep(15)

bot.polling(none_stop=True)
