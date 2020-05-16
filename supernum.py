import sqlite3 as sql
from sqlite3 import Error


__connection = None

def get_connection():
    global __connection
    __connection = sql.connect('supernum.db')
    return __connection


def init_db(force: bool = False):
    conn = get_connection()
    c    = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS supernum')
    c.execute('''
            CREATE TABLE IF NOT EXISTS supernum(
            user_id               INTEGER,
            first                 INTEGER DEFAULT NULL,
            second                INTEGER DEFAULT NULL,
            third                 INTEGER DEFAULT NULL,
            fourth                INTEGER DEFAULT NULL
            )
        ''')
    conn.commit()
    c.close()
    conn.close()




def run_sen(user_id: int, index:int,num_:int):
    conn = get_connection()
    c = conn.cursor()
    print('num_', num_)
    if index == 1:
        num = str(num_)[0]
        print('num',num)
        c.execute('UPDATE supernum SET first = ? WHERE user_id = ?', (num, user_id))
        conn.commit()
        c.close()
        conn.close()
        return num
    elif index == 2:
        num = str(num_)[1]
        print('num', num)
        c.execute('UPDATE supernum SET second = ? WHERE user_id = ?', (num, user_id))
        conn.commit()
        c.close()
        conn.close()
        return num
    elif index == 3:
        num = str(num_)[2]
        print('num', num)
        c.execute('UPDATE supernum SET third = ? WHERE user_id = ?', (num, user_id))
        conn.commit()
        c.close()
        conn.close()
        return num
    elif index == 4:
        num = str(num_)[3]
        print('num', num)
        c.execute('UPDATE supernum SET fourth = ? WHERE user_id = ?', (num, user_id))
        conn.commit()
        c.close()
        conn.close()
        return num
    else:
        print('else______ none')


def add_id(user_id:int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM supernum WHERE user_id = ?', (user_id,))
    select = c.fetchone()
    if select is None:
        try:
            c.execute('INSERT INTO supernum (user_id) VALUES (?)',(user_id,))
        except Error:
            print(Error)
        conn.commit()
        c.close()
        conn.close()
    else:
        c.close()
        conn.close()


def drop_num(user_id:int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE supernum SET (first,second ,third , fourth) = (NULL, NULL, NULL, NULL) WHERE user_id = ?',(user_id,))
    conn.commit()
    c.close()
    conn.close()


def use_product(user_id: int, id_num: int, num_: int):
    conn = get_connection()
    c = conn.cursor()
    try:
        if id_num == 1:
            num = str(num_)[0]
            c.execute('UPDATE supernum SET first = ? WHERE user_id = ?', (num, user_id))
            conn.commit()
            c.close()
            conn.close()
            return num
        elif id_num == 2:
            num = str(num_)[1]
            c.execute('UPDATE supernum SET second = ? WHERE user_id = ?', (num, user_id))
            conn.commit()
            c.close()
            conn.close()
            return num
        elif id_num == 3:
            num = str(num_)[2]
            c.execute('UPDATE supernum SET third = ? WHERE user_id = ?', (num, user_id))
            conn.commit()
            c.close()
            conn.close()
            return num
        elif id_num == 4:
            num = str(num_)[3]
            c.execute('UPDATE supernum SET fourth = ? WHERE user_id = ?', (num, user_id))
            conn.commit()
            c.close()
            conn.close()
            return num
    except Error as e:
        print(e)


def run_srn(user_id:int, id_num:int, num_:int):
    conn = get_connection()
    c    = conn.cursor()
    try:
        if id_num == 1:
            num = str(num_)[0]
            c.execute('UPDATE supernum SET first = ? WHERE user_id = ?', (num,user_id))
            conn.commit()
            c.close()
            conn.close()
            return num
        elif id_num == 2:
            num = str(num_)[1]
            c.execute('UPDATE supernum SET second = ? WHERE user_id = ?', (num, user_id))
            conn.commit()
            c.close()
            conn.close()
            return num
        elif id_num == 3:
            num = str(num_)[2]
            c.execute('UPDATE supernum SET third = ? WHERE user_id = ?', (num, user_id))
            conn.commit()
            c.close()
            conn.close()
            return num
        elif id_num == 4:
            num = str(num_)[3]
            c.execute('UPDATE supernum SET fourth = ? WHERE user_id = ?', (num, user_id))
            conn.commit()
            c.close()
            conn.close()
            return num
    except Error as e:
        print(e)

def get_result(user_id:int):
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM supernum WHERE user_id = ?',(user_id,))
    except Error as e:
        print(e)
    result = c.fetchone()
    print('result!',result)
    sum = ''
    for i in result:
        if i == None:
            sum += (' '.join('?'))
            print('none:::',sum)
        else:
            if i > 10:
                continue
            else:
                sum += (' '.join(str(i)))
                print('else:::', sum)
    c.close()
    conn.close()
    return sum

if __name__ == '__main__':
    init_db()