# bot_module.py
from datetime import datetime
import sqlite3
from telebot import TeleBot, types

# Bot Token
BOT_TOKEN = '7574557958:AAHTGzsIT9_fYM-Ls54Z18pUg05RF1_e20Y'

# Initialize bot
bot = TeleBot(BOT_TOKEN)

# Database path
db_path = 'Risk_Sincerity.db'

def initialize_database():
    """Function to create the database and table if not exists."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            first_name TEXT,
            last_name TEXT,
            username TEXT,
            registration_date TEXT
        )''')
        conn.commit()

def start_handler(message: types.Message):
    """Handles /start command and stores user data in the database."""
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    registration_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT INTO users (user_id, first_name, last_name, username, registration_date)
                               VALUES (?, ?, ?, ?, ?)''',
                           (user_id, first_name, last_name, username, registration_date))
            conn.commit()
        except sqlite3.IntegrityError:
            print(None)
