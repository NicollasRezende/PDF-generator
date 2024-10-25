from frameworks_and_drivers.database import DatabaseConnection

class UserRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def add_user(self, user):
        query = 'INSERT INTO users (name, email, age) VALUES (%s, %s, %s) RETURNING id'
        params = (user.name, user.email, user.age)
        user_id = self.db.execute_query(query, params)
        return user_id
