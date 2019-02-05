
from models import User
import argparse
from clcrypto import check_password, password_hash
from database import get_connection, get_cursor
#
# parser = argparse.ArgumentParser(description="Nasza aplikacja, która coś robi")
# parser.add_argument('-u', '--user', type=str, help="Pomoc komendy. Użycie -u nazwa użytkownika")
# parser.add_argument('-p', '--password', type=str, help="Pomoc komendy. Użycie -p hasło")
# parser.add_argument('-n', '--new_pass', type=str, help="Pomoc komendy. Nastawienie nowego hasła")
# parser.add_argument('-l','--list', type=str, help="Pomoc komendy. Wylistowanie wszystkich użytkowników")
# parser.add_argument('-d','--delete', type=str, help="Pomoc komendy. Konto użytkownika do usunięcia")
# args = parser.parse_args()
#
# if __name__ == '__main__':
    # u = args.user
    # p = args.password
    # n = args.new_pass
    # d = args.delete
    # l = args.list
    #
    #
    # def manage_user(u,p,n,d,l):
    #     if u and p and not n and not d and not l:
    #         cnx = get_connection()
    #         crs = get_cursor(cnx)
    #         user = User.load_user_by_username(crs,u)
    #         if user:
    #             print("Błąd: użytkownik o podanym emailu już istnieje")
    #         elif len(p) < 8:
    #             print("Hasło powinno składać się z co najmniej 8 znaków")
    #         else:
    #             user = User()
    #             user.username = u
    #             user.set_password(p)
    #             user.save_to_db(crs)
    #             print(f"Użytkownik {u} został dodany")
    #         crs.close()
    #         cnx.close()
    #     elif u and p and n and not d and not l:
    #         cnx = get_connection()
    #         crs = get_cursor(cnx)
    #         user = User.load_user_by_username(crs, u)
    #         if len(n) < 8:
    #             print("Hasło musi zawierać co najmniej 8 znaków")
    #         else:
    #             if user and user.check_password(p):
    #                 user.set_password(n)
    #                 user.save_to_db(crs)
    #                 print(f"Hasło użytkownika {u} zostało zmienione")
    #             else:
    #                 print("Niepoprawne dane logowania")
    #         crs.close()
    #         cnx.close()
    #     elif u and p and not n and d and not l:
    #         cnx = get_connection()
    #         crs = get_cursor(cnx)
    #         user = User.load_user_by_username(crs, u)
    #         if user and user.check_password(p):
    #             user.delete(crs)
    #             print(f"Użytkownik {u} został usunięty")
    #         else:
    #             print("Niepoprawne dane logowania")
    #         crs.close()
    #         cnx.close()
    #     elif u and p and not n and not d and l:
    #         cnx = get_connection()
    #         crs = get_cursor(cnx)
    #         users = User.load_all_users(crs)
    #         for user in users:
    #             print("Nazwa użytkownika: {}".format(user.username))
    #         crs.close()
    #         cnx.close()
    #     else:
    #         print("Niepoprawna operacja")
    #
    #
    #
    # manage_user(u,p,n,d,l)
    #
    # cnx = get_connection()
    # cursor = get_cursor(cnx)
    #
    # sql = """SELECT message.id, message.from_id, message.to_id, message.creation_date, message.text FROM users JOIN message ON \
    #                 users.id = message.from_id WHERE message.to_id=%s ORDER BY message.creation_date ASC;"""
    # cursor.execute(sql, (10,))
    # for result in cursor.fetchall():
    #     print(str(result["creation_date"]))
    #
    # cursor.close()
    # cnx.close()






   # loaded_users = User.load_all_users(cursor)
   #
   # if args.user and args.password:
   #     print(f"Podany login: {args.user} a podane hasło to: {args.password}")
   #
   #     loaded_user = User.load_user_by_username(cursor, args.user)
   #     if loaded_user and check_password(args.password, loaded_user.hashed_password):
   #         print("Poprawne dane")
   #     else:
   #         print("Błędne dane")
   #
   # connection.close()

 # user = User()
#     # user.username = 'Janusz'
#     # user.email = 'janusz@asd.pl'
#     # user.set_password('tajne123')
#     # user.save_to_db(cursor)

 # users = User.load_all_users(cursor)
    # print(users)


            # if u and p and not n and not d and not e and l:
            # cnx = get_connection()
            # crs = get_cursor(cnx)
            # user = User.load_user_by_username(crs,u)
            # if not user or not user.check_password(p):
            #     print("Niepoprawne dane logowania")
            # else:
            #     results = User.load_all_users(crs)
            #     print("Lista istniejących użytkowników:")
            #     for result in results:
            #         print("id: {}, username: {}".format(result.id, result.username))
            # crs.close()
            # cnx.close()