import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="junction.proxy.rlwy.net",
            dbname="railway",
            user="postgres",
            password="QLrtaCWqyegozyvpBuPoHxQGwqTkVyNE",
            port="44943",
        )

    def execute_query(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        user_id = cursor.fetchone()[0]
        self.connection.commit()
        cursor.close()
        return user_id

    def get_user_by_id(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        return {"id": user[0], "name": user[1], "email": user[2], "age": user[3]} if user else None
