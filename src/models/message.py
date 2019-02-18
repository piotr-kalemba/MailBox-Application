import sys

sys.path.append("..")

# CREATE TABLE message (
#        id serial NOT NULL,
#        from_id int NOT NULL,
#        to_id int NOT NULL,
#        text text,
#        creation_date timestamp default current_timestamp,
#        FOREIGN KEY(from_id) REFERENCES users(id) ON DELETE CASCADE,
#        FOREIGN KEY(to_id) REFERENCES users(id) ON DELETE CASCADE,
#        PRIMARY KEY(id)
#      )

class Message:
    # __id = None
    # from_id = None
    # to_id = None
    # text = None
    # creation_date = None


    def __init__(self):
        self.__id = -1
        self.from_id = 0
        self.to_id = 0
        self.text = 0
        self.creation_date = 0

    @property
    def id(self):
        return self.__id


    def save_to_db(self, cursor):
        if self.__id == -1:
            sql = """INSERT INTO message(from_id, to_id, text)
                     VALUES(%s, %s, %s) RETURNING id"""
            values = (self.from_id, self.to_id,self.text)
            cursor.execute(sql, values)
            self.__id = cursor.fetchone()['id']
            return True
        else:
            sql = """UPDATE message SET from_id=%s, to_id=%s, text=%s, creation_date=%s WHERE id=%s"""
            values = (self.from_id, self.to_id, self.text, self.creation_date, self.id)
            cursor.execute(sql, values)
            return True

    @staticmethod
    def load_message_by_id(cursor, message_id):
        sql = "SELECT id, from_id, to_id, text, creation_date FROM message WHERE id=%s"
        cursor.execute(sql, (message_id,))  # (user_id, ) - bo tworzymy krotkę
        data = cursor.fetchone()
        if data:
            loaded_message = Message()
            loaded_message.__id = data['id']
            loaded_message.from_id = data['from_id']
            loaded_message.to_id = data['to_id']
            loaded_message.text = data['text']
            loaded_message.creation_date = data['creation_date']
            return loaded_message
        else:
            return None

    @staticmethod
    def load_all_messages_for_user(cursor,user_id):
        sql = """SELECT message.id, message.from_id, message.to_id, message.creation_date, message.text FROM users JOIN message ON \
        users.id = message.from_id WHERE message.to_id=%s ORDER BY message.creation_date ASC;"""
        cursor.execute(sql,(user_id,))
        ret = []
        for result in cursor.fetchall():
            message = Message()
            message.__id = result["id"]
            message.from_id = result["from_id"]
            message.to_id = result["to_id"]
            message.creation_date = str(result["creation_date"])
            message.text = result["text"]
            ret.append(message)
        return ret

    @staticmethod
    def load_all_messages(cursor):
        sql = """SELECT * FROM message ORDER BY creation_date;"""
        cursor.execute(sql)
        ret = []
        for message in cursor.fetchall():
            loaded_message = Message()
            loaded_message.__id = message['id']
            loaded_message.from_id = message['from_id']
            loaded_message.to_id = message['to_id']
            loaded_message.text = message['text']
            loaded_message.creation_date = message['creation_date']
            ret.append(loaded_message)
        return ret

    def sender(self,cursor):
        sql = """SELECT users.username FROM users JOIN message ON message.from_id = users.id WHERE message.from_id=%s"""
        cursor.execute(sql,(self.from_id,))
        sender = cursor.fetchone()["username"]
        return sender



    def recepient(self, cursor):
        sql = """SELECT users.username FROM users JOIN message ON message.to_id = users.id WHERE message.to_id=%s"""
        cursor.execute(sql, (self.to_id,))
        recepient = cursor.fetchone()["username"]
        return recepient