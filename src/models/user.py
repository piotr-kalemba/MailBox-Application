import sys

sys.path.append("..")

from clcrypto import password_hash, check_password

# CREATE TABLE users (
#   id serial NOT NULL,
#   username VARCHAR(255) UNIQUE NOT NULL,
#   hashed_password VARCHAR(255) NOT NULL,
#   PRIMARY KEY (id)
# );
#


class User:
    __id = None
    username = None
    __hashed_password = None


    def __init__(self):
        self.__id = -1
        self.username = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password, salt=None):
        self.__hashed_password = password_hash(password, salt)

    def save_to_db(self, cursor):
        if self.__id == -1:
            sql = """INSERT INTO users(username, hashed_password)
                     VALUES(%s, %s) RETURNING id"""
            values = (self.username, self.hashed_password)
            cursor.execute(sql, values)
            self.__id = cursor.fetchone()['id']
            return True
        else:
            sql = """UPDATE users SET username=%s, hashed_password=%s WHERE id=%s"""
            values = (self.username, self.hashed_password, self.id)
            cursor.execute(sql, values)
            return True

    @staticmethod
    def load_user_by_id(cursor, user_id):
        sql = "SELECT id, username, hashed_password FROM users WHERE id=%s"
        cursor.execute(sql, (user_id,))  # (user_id, ) - bo tworzymy krotkę
        data = cursor.fetchone()
        if data:
            loaded_user = User()
            loaded_user.__id = data['id']
            loaded_user.username = data['username']
            loaded_user.__hashed_password = data['hashed_password']
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        sql = """SELECT * FROM users ORDER BY username;"""
        cursor.execute(sql)
        ret = []
        for user in cursor.fetchall():
            loaded_user = User()
            loaded_user.__id = user['id']
            loaded_user.username = user['username']
            loaded_user.__hashed_password = user['hashed_password']
            ret.append(loaded_user)
        return ret

    def delete(self, cursor):
        sql = "DELETE FROM users WHERE id=%s"
        cursor.execute(sql, (self.__id,))
        self.__id = -1
        return True

    @staticmethod
    def load_user_by_username(cursor, username):
        sql = "SELECT id, username, hashed_password FROM users WHERE username=%s"
        cursor.execute(sql, (username,))
        data = cursor.fetchone()
        if data:
            loaded_user = User()
            loaded_user.__id = data['id']
            loaded_user.username = data['username']
            loaded_user.__hashed_password = data['hashed_password']
            return loaded_user
        else:
            return None

    def check_password(self, password):
        return check_password(password, self.__hashed_password)