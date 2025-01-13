import sqlite3

def tables():
    conn = sqlite3.connect('Risk_Sincerity.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Risk(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Tasks VARCHAR(50) NOT NULL)''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sincerity(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Questions VARCHAR(50) NOT NULL)''')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS Names(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ChatID INTEGER NOT NULL,
            Names TEXT)''')

    conn.commit()
    cursor.close()
    conn.close()

tables()