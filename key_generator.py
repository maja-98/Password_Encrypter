from cryptography.fernet import Fernet
import sqlite3,os
connection=sqlite3.connect('key.db')
cursor=connection.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS KEY
(Key BLOB)''')

confirmation = input('Are you sure you want to create/change a key (y/n): ').lower()


if confirmation == 'y':
    confirmation=input('''Warning: This will remove your old key and
    it will cause for losing all your old saved Passwords with that key!!!
    (y/n): ''').lower()
if confirmation == 'y':
    cursor.execute(''' DELETE FROM KEY ''')
    k=Fernet.generate_key()

    cursor.execute('''INSERT INTO KEY(Key) VALUES (?)''',(k,))
    os.remove('passwords.csv')
    print("New Key is generated...")
    print("All your old passwords are deleted")
    
else :
    print('Your key is still the same')
connection.commit()
cursor.close()
