
from models import User
import argparse
from database import get_connection, get_cursor

parser = argparse.ArgumentParser(description="Nasza aplikacja, która coś robi")
parser.add_argument('-u', '--user', type=str, help="Pomoc komendy. Użycie -u nazwa użytkownika")
parser.add_argument('-p', '--password', type=str, help="Pomoc komendy. Użycie -p hasło")
parser.add_argument('-n', '--new_pass', type=str, help="Pomoc komendy. Nastawienie nowego hasła")
parser.add_argument('-l','--list', type=str, help="Pomoc komendy. Wylistowanie wszystkich użytkowników")
parser.add_argument('-d','--delete', type=str, help="Pomoc komendy. Konto użytkownika do usunięcia")
args = parser.parse_args()

if __name__ == '__main__':
    u = args.user
    p = args.password
    n = args.new_pass
    d = args.delete
    l = args.list


    def manage_user(u,p,n,d,l):
        cnx = get_connection()
        crs = get_cursor(cnx)
        if u and p and not n and not d and not l:
            user = User.load_user_by_username(crs,u)
            if user:
                print("Błąd: użytkownik o podanym loginie już istnieje")
            elif len(p) < 8:
                print("Hasło powinno składać się z co najmniej 8 znaków")
            else:
                user = User()
                user.username = u
                user.set_password(p)
                user.save_to_db(crs)
                print(f"Użytkownik {u} został dodany")
        elif u and p and n and not d and not l:
            user = User.load_user_by_username(crs, u)
            if len(n) < 8:
                print("Hasło musi zawierać co najmniej 8 znaków")
            else:
                if user and user.check_password(p):
                    user.set_password(n)
                    user.save_to_db(crs)
                    print(f"Hasło użytkownika {u} zostało zmienione")
                else:
                    print("Niepoprawne dane logowania")
        elif u and p and not n and d and not l:
            user = User.load_user_by_username(crs, u)
            if user and user.check_password(p):
                user.delete(crs)
                print(f"Użytkownik {u} został usunięty")
            else:
                print("Niepoprawne dane logowania")
        elif u and p and not n and not d and l:
            user = User.load_user_by_username(crs, u)
            if user and user.check_password(p):
                users = User.load_all_users(crs)
                for user in users:
                    print("Nazwa użytkownika: {}".format(user.username))
            else:
                print("Niepoprawne dane logowania")
        else:
            print("Niepoprawna operacja")
        crs.close()
        cnx.close()

    manage_user(u,p,n,d,l)

