import sqlite3 as sql
from sqlite3 import Error

__connection = None

def get_connection():
    global __connection
    __connection = sql.connect('solo_games.db')
    return __connection


def init_db(force: bool = False):
    conn = get_connection()
    c    = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS solo_games')
    c.execute('''
            CREATE TABLE IF NOT EXISTS solo_games(
            id_user             INTEGER,
            num                 INTEGER DEFAULT '0',
            play                INTEGER DEFAULT '0'
            )
        ''')
    conn.commit()
    c.close()
    conn.close()

def add_num(user_id: int, num: int):
    conn = get_connection()
    c    = conn.cursor()

    try:
        c.execute('UPDATE solo_games SET num = ? WHERE id_user = ?', (num,user_id))
    except Error as e:
        print(e)

    conn.commit()
    c.close()
    conn.close()

def add_user(user_id:int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM solo_games WHERE id_user = ?', (user_id,))
    if c.fetchone() is None:
        try:
            c.execute('INSERT INTO solo_games (id_user) VALUES (?)', (user_id,))
        except Error as e:
            print(e)
        conn.commit()
        return True
    else:
        c.close()
        conn.close()
        return True


def get_num(user_id: int):
    conn = get_connection()
    c    = conn.cursor()
    try:
        c.execute('SELECT * FROM solo_games WHERE id_user = ?', (user_id,))
    except Error as e:
        print(e)
    res = c.fetchone()[1]
    c.close()
    conn.close()
    return res



def del_num(user_id: int):
    conn = get_connection()
    c    = conn.cursor()
    try:
        c.execute('UPDATE solo_games SET num = 0 WHERE id_user = ?', (user_id,))
    except Error as e:
        print(e)
    conn.commit()
    c.close()
    conn.close()

def play(user_id: int, plaing: bool):
    conn = get_connection()
    c    = conn.cursor()
    if plaing:
        try:
            c.execute('UPDATE solo_games SET play = 1 WHERE id_user = ?', (user_id,))
            conn.commit()
            c.close()
            conn.close()
        except Error as e:
            print(e)
    else:
        try:
            c.execute('UPDATE solo_games SET play = 0 WHERE id_user = ?', (user_id,))
            conn.commit()
            c.close()
            conn.close()
        except Error as e:
            print(e)


def get_playing(user_id: int):
    conn = get_connection()
    c    = conn.cursor()
    c.execute('SELECT play FROM solo_games WHERE id_user = ?', (user_id,))
    res = c.fetchone()
    if res == (1,):
        c.close()
        conn.close()
        return True
    else:
        c.close()
        conn.close()
        return False

def get_user(id_user: int):
    conn = get_connection()
    c    = conn.cursor()
    try:
        c.execute('SELECT * FROM solo_games WHERE id_user = ?', (id_user,))
    except Error as e:
        print(e)
    result = c.fetchone()
    c.close()
    conn.close()
    return result

if __name__ == '__main__':
    init_db(True)