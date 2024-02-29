from db_config import db_name, password, user, host
import psycopg2


def drop_cook_form():
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            drop_query = '''DROP table IF EXISTS cook_form cascade'''
            cursor.execute(drop_query)
            db_connect.commit()
            print('+ cook_form dropped')


def drop_users():
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            drop_query = '''DROP table IF EXISTS users cascade'''
            cursor.execute(drop_query)
            db_connect.commit()
            print('+ users dropped')


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
            print('+ users created')


def create_cook_table():
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            create_table = '''
            CREATE TABLE IF NOT EXISTS CookForm(
            id uuid PRIMARY KEY,
            user_id uuid NOT NULL,
            title varchar (120) NOT NULL,
            description varchar (3000) NOT NULL,
            active bool NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
            )'''
            cursor.execute(create_table)
            db_connect.commit()
            print('+ cook_form created')


drop_cook_form()
drop_users()
create_users()
create_cook_table()
