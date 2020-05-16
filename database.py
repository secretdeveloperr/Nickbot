import sqlite3 as sql
from sqlite3 import Error


__connection = None

def get_users_db():
    global __connection
    __connection = sql.connect('users.db')
    return __connection

def init_db(force: bool = False):
    conn = get_users_db()
    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS users')
    c.execute('''
        CREATE TABLE IF NOT EXISTS users(
        user_id     INTEGER ,
        name        VARCHAR ,
        username    VARCHAR ,
        money       INTEGER DEFAULT '0',
        total_win   INTEGER DEFAULT '0',
        total_play  INTEGER DEFAULT '0',
        srn         INTEGER DEFAULT '0',
        sen         INTEGER DEFAULT '0',
        stn         INTEGER DEFAULT '0',
        chat_id     INTEGER 
        )
    ''')
    conn.commit()
    c.close()
    conn.close()





def buy(user_id: int, price:int,name:str):
    conn = get_users_db()
    c = conn.cursor()
    if name == 'stn':
        c.execute('UPDATE users SET (money,stn) = (money - ?, stn+1) WHERE user_id = ?', (price,user_id))
        conn.commit()
        c.close()
        conn.close()
        return True
    elif name == 'sen':
        c.execute('UPDATE users SET (money,sen) = (money - ?, sen+1) WHERE user_id = ?', (price, user_id))
        conn.commit()
        c.close()
        conn.close()
        return True
    elif name == 'srn':
        c.execute('UPDATE users SET (money,srn) = (money - ?, srn+1) WHERE user_id = ?', (price, user_id))
        conn.commit()
        c.close()
        conn.close()
        return True
    else:
        print('Error buy!')




def use_product(user_id: int, srn: bool,sen:bool,stn: bool):
    conn = get_users_db()
    c = conn.cursor()
    if srn:
        c.execute('UPDATE users SET (srn) = (srn-1) WHERE  user_id = ?', (user_id,))
        conn.commit()
        c.close()
        conn.close()
    elif sen:
        c.execute('UPDATE users SET (sen) = (sen-1) WHERE  user_id = ?', (user_id,))
        conn.commit()
        c.close()
        conn.close()
    elif stn:
        c.execute('UPDATE users SET (stn) = (srn-1) WHERE  user_id = ?', (user_id,))
        conn.commit()
        c.close()
        conn.close()
    else:
        print('Error!')
        c.close()
        conn.close()


def get_product(user_id: int, srn: bool,sen:bool,stn: bool):
    conn = get_users_db()
    c = conn.cursor()
    if srn:
        c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        result = c.fetchone()[6]
        c.close()
        conn.close()
        return result
    elif sen:
        c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        result = c.fetchone()[7]
        c.close()
        conn.close()
        return result
    elif stn:
        c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        result = c.fetchone()[8]
        c.close()
        conn.close()
        return result
    else:
        print('Error!')
        c.close()
        conn.close()


def add_money(user_id: int, total: int,):
    conn = get_users_db()
    c = conn.cursor()
    c.execute('UPDATE users SET money = ? WHERE user_id = ?', (total,user_id))
    conn.commit()
    c.close()
    conn.close()


def get_money(user_id: int, price: int, get_money: bool):
    conn = get_users_db()
    c = conn.cursor()
    if get_money:
        c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        result = c.fetchone()[3]
        c.close()
        conn.close()
        return result
    else:
        c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        result = c.fetchone()[3]

        if result >= price:
                c.close()
                conn.close()
                return True
        else:
                c.close()
                conn.close()
                return False


def check_reg(user_id: int, name: str , username: str,chat_id:int):
    conn = get_users_db()
    c = conn.cursor()
    result = None
    if c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)):
        result = c.fetchone()
    if result is None:
        return register(user_id,name,username,chat_id)
    else:
        return True


def register(user_id: int, name: str , username: str,chat_id:int):
    conn = get_users_db()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (user_id , name, username, chat_id)  VALUES (?,?,?,?)', (user_id, name, username,chat_id))
    except Error as e:
        print(e)
    conn.commit()
    c.close()
    conn.close()
    return True

def get_info(user_id: int):
    conn = get_users_db()
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    except Error as e:
        print(e)
    res = c.fetchone()
    c.close()
    conn.close()
    return res

def lose(user_id: int):
    conn = get_users_db()
    c = conn.cursor()
    try:
        c.execute('UPDATE users SET (total_play) = (total_play+1 ) WHERE user_id = ?', (user_id,))
    except Error as e:
        print(e)
    conn.commit()
    c.close()
    conn.close()

def win(user_id: int):
    conn = get_users_db()
    c = conn.cursor()
    try:
        c.execute('UPDATE users SET (money,total_win,total_play) = (money+5,total_win+1,total_play+1 ) WHERE user_id = ?', (user_id,))
    except Error as e:
        print(e)
    conn.commit()
    c.close()
    conn.close()

if __name__ == '__main__':
    pass

