Plik users.py zawiera program do obsługi użytkowników.
Pominąłem w kodzie pole email, bo w scenariuszu i tak
użytkownik jest identyfikowany za pomocą swojej nazwy
(username ma w moim kodzie atrybut UNIQUE).
Plik models/user.py zawiera w klasie User dodatkową
metodę 'check_password' przyjmującą jeden argument 'password'
i sprawdzającą czy jest on poprawnym hasłem użytkownika.
Plik messages.py zawiera program do obsługi przesyłania
wiadomości zgodny ze scenariuszem.
Plik models/message.py zawiera klasę Message spełniającą
wymagania oraz metody sender i recepient zwracające
odpowiednio nazwę nadawcy oraz odbiorcy wiadomości.
Metoda sender jest użyta w pliku messages.py.
Plik main.py nie zawiera kodu.

git@github.com:piotr-kalemba/Workshops2.git