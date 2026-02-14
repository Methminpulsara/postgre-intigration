from db import db_connection()

def create_user(name:str, email:str):
    with get_db_con() as db_connection:
        with db_connection.cursor() as cursor:
            cursor.ececute(
                """
                INSERT INTO USERS (name , email)
                VALUES (%s , %s)
                RETURNING id , name ,email
                """,
                (name, email)
            )
            return (name,email)


def get_by_id(id):
    with get_db_con() as db_connection:
        with db_connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM users
                WHERE id = %s
                """,
                (id,)
            )
            return cursor.fetcone()

def get_all(id):
    with get_db_con() as db_connection:
        with db_connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT name , email and password  FROM users
                ORDER BY name
                """,
            )
            return cursor.fetcall()
