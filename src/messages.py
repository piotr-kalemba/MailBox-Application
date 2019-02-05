from models import User, Message
import argparse
from database import get_connection, get_cursor

parser = argparse.ArgumentParser(description="Nasza aplikacja, która coś robi")
parser.add_argument('-u', '--user', type=str, help="Pomoc komendy. Użycie -u login")
parser.add_argument('-p', '--password', type=str, help="Pomoc komendy. Użycie -p hasło")
parser.add_argument('-l','--list', type=str, help="Pomoc komendy. Wylistowanie wszystkich użytkowników")
parser.add_argument('-t','--to', type=str, help="Pomoc komendy. Nastawienie nzawy użytkownika, do którego chcemy wysłać wiadomość")
parser.add_argument('-s','--send', type=str, help="Pomoc komendy. Treść komunikatu do  wybranego użytkownika")
args = parser.parse_args()

if __name__ == '__main__':
    u = args.user
    p = args.password
    l = args.list
    t = args.to
    s = args.send

    def manage_message(u,p,l,t,s):
        cnx = get_connection()
        crs = get_cursor(cnx)
        if u and p and l and not t and not s:
            user = User.load_user_by_username(crs,u)
            if user and user.check_password(p):
                user_id = user.id
                messages = Message.load_all_messages_for_user(crs, user_id)
                for msg in messages:
                    print("Data: {}\nNadawca: {}\nTreść: {}".format(msg.creation_date,msg.sender(crs),msg.text))
            else:
                print("Błędne dane logowania")
        elif u and p and not l and t:
            user = User.load_user_by_username(crs, u)
            if not user or not user.check_password(p):
                print("Błędne dane logowania")
            else:
                recepient = User.load_user_by_username(crs, t)
                if not recepient:
                    print("Użytkownik podany jako odbiorca wiadomości nie istnieje")
                else:
                    if not s:
                        print("Nie podano treści wiadomości")
                    else:
                        msg = Message()
                        msg.from_id = user.id
                        msg.to_id = recepient.id
                        msg.text = s
                        msg.save_to_db(crs)
                        print(f"Wiadomość do użytkownika {t} została wysłana")
        else:
            print("Niepoprawna operacja")
        crs.close()
        cnx.close()

    manage_message(u,p,l,t,s)


