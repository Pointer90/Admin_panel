from sqlite3 import connect
import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password):
    connect = None
    try:
        connect = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )

        cursor = connect.cursor()

        print('Подключение к базе данных - успешно!')

    except Error as e:
        print(
            f'Подключение к базе данных - Ошибка! ({e})')

    return connect, cursor


def show_students():
    connect, cursor = create_connection('26.157.28.233', 'root', 'root')

    try:
        cursor.execute('''Use admin_panel''')
        cursor.execute('''SELECT * FROM Students ''')
        print(cursor.fetchall())

    except Error as e:
        print(f'Ошибка — {e}')

    cursor.close()
    connect.close()


def insert_student(SID, FIO, Group, Faculty, CID):
    connect, cursor = create_connection('26.157.28.233', 'root', 'root')

    try:
        cursor.execute('''Use admin_panel''')
        cursor.execute(
            f'INSERT INTO Students (Student_ID, FIO, Group_ID, Faculty, Course_ID) VALUES ("{SID}", "{FIO}", "{Group}", "{Faculty}", "{CID}");')
        connect.commit()
        print(
            f'Пользоваетль {FIO} успешно добавлен!')

    except Error as e:
        print(f'Не удалось! — {e}')

    cursor.close()
    connect.close()


def delete_student():
    connect, cursor = create_connection('26.157.28.233', 'root', 'root')

    try:
        cursor.execute('''Use admin_panel''')
        cursor.execute('''Delete From Students''')
        connect.commit()
        print('Пользователи удалены успешно!')

    except Error as e:
        print(f'Не удалось — {e}')

    cursor.close()
    connect.close()
