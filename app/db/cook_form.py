from .db_config import db_name, password, user, host
import psycopg2
import psycopg2.extras


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


def insert_cook_form_info(info: dict[str: str | int]):
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            values = (info['id'], info['user_id'], info['title'], info['description'], info['active'])
            insert_query = '''
            INSERT INTO CookForm (
            id,
            user_id,
            title,
            description,
            active)  VALUES(%s, %s, %s, %s, %s)'''
            cursor.execute(insert_query, values)
            db_connect.commit()


def update_cook_form_info(user_id: str, info: dict[str: str | bool]) -> None:
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            for key, value in info.items():
                cursor.execute(f'''UPDATE CookForm set {key} = %s where id=%s''', (value, user_id))
                db_connect.commit()


def db_get_my_all_cook_form(user_id: str, limit: int, offset: int) -> tuple[list[str]]:
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            select_query = '''
            SELECT title, description FROM CookForm 
            WHERE user_id = %s
            LIMIT %s
            OFFSET %s
            '''
            cursor.execute(select_query, (user_id, limit, offset))
            result = cursor.fetchall()
            return result


def db_get_all_cook_form(limit: int, offset: int) -> tuple[list[str]]:
    with psycopg2.connect(dbname=db_name,
                          user=user,
                          password=password,
                          host=host) as db_connect:
        with db_connect.cursor() as cursor:
            select_query = '''
            SELECT title, description FROM CookForm 
            WHERE active is true
            LIMIT %s
            OFFSET %s
            '''
            cursor.execute(select_query, (limit, offset))
            result = cursor.fetchall()
            return result
