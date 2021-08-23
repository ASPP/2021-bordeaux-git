import os
import json
PWDB_FILENAME = 'pwdb.json'

def get_credentials():
    username = input('Type the username: ')
    password = input('Type the password: ')
    return username, password

def authenticate(user, password, pwdb):
    if user in pwdb:
        if password == pwdb[user]:
            print('Successfully authenticated!')
        else:
            print('Wrong password!!')
    else:
        add = input('Add user to the db? ')
        if add == 'y':
            pwdb[user] = password
        else:
            pass
    return

def write_pwdb(pwdb):
     with open(PWDB_FILENAME, 'w') as fh:
        json.dump(pwdb, fh)

def read_pwdb():
    if os.path.exists(PWDB_FILENAME):
        with open(PWDB_FILENAME, 'r') as fh:
            pwdb = json.load(fh)
    else:
        pwdb = {}
        write_pwdb(pwdb)
    return pwdb


pwdb = read_pwdb()
user, password = get_credentials()
authenticate(user, password, pwdb)
write_pwdb(pwdb)
print(pwdb)
