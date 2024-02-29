from .db_config import db_name, password, user, host
import psycopg2
import psycopg2.extras
import datetime


def create_users():
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            create_table = '''CREATE TABLE IF NOT EXISTS users(
            id uuid PRIMARY KEY,
            first_name varchar (30) NOT NULL,
            last_name varchar (30) NOT NULL,
            birthday timestamp NOT NULL,
            city varchar (80) NOT NULL,
            sex varchar (1) NOT NULL,
            email varchar (120) UNIQUE NOT NULL,
            password_hash varchar (120) NOT NULL,
            create_date timestamp,
            update_date timestamp
            )'''
            cursor.execute(create_table)
            db_connect.commit()


def insert_user_info(info: dict[str: str | int]) -> None:
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            values_to_insert = (info['id'], info['first_name'], info['last_name'], info['birthday'], info['city'],
                                info['sex'], info['email'], info['password'], now, now)
            insert_query = f'''INSERT INTO users(
            id,
            first_name,
            last_name,
            birthday,
            city,
            sex,
            email,
            password_hash,
            create_date,
            update_date)  
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(insert_query, values_to_insert)
            db_connect.commit()


def db_update_user_info(user_id: str, info: dict[str: str | int]) -> None:
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            for key, value in info.items():
                cursor.execute(f'''UPDATE users set {key} = %s where id=%s''', (value, user_id))
                db_connect.commit()


def get_user_by_email(email: str) -> dict:
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            read_query = '''SELECT * from users where email =%s'''
            cursor.execute(read_query, (email,))
            result = cursor.fetchone()
            return result


def get_user_by_id(user_id: str) -> dict:
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            read_query = '''SELECT * from users where id =%s'''
            cursor.execute(read_query, (user_id,))
            result = cursor.fetchone()
            return result
