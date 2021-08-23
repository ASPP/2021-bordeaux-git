import os
import json
import random
import string
from getpass import getpass

PWDB_FILENAME = 'pwdb.json'
SALT_LENGTH = 5
VALID_CHAR = string.ascii_letters + string.digits + string.punctuation


def get_credentials():
    username = input('Type the username: ')
    password = getpass('Type the password: ')
    return username, password

def add_user(user, password, pwdb):
    salt = get_random_salt()
    pwdb[user] = (salt, pwhash(salt+password))
    write_pwdb(pwdb)
    return

def authenticate(user, password, pwdb):
    if user in pwdb:
        salt, hash_ = pwdb[user]
        if pwhash(salt+password) == hash_:
            print('Successfully authenticated!')
        else:
            print('Wrong password!!')
    else:
        answer = input('Add user to the db? ')
        if answer == 'y':
            add_user(user, password, pwdb)

    return

def get_random_salt():
    char_list = random.choices(VALID_CHAR, k=SALT_LENGTH)
    salt = ''.join(char_list)
    return salt

def pwhash(password):
    hash_ = 0
    for idx, char in enumerate(password):
        hash_ += (idx+1)*ord(char)
    return hash_


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


if __name__ == "__main__":
    pwdb = read_pwdb()
    user, password = get_credentials()
    authenticate(user, password, pwdb)
    write_pwdb(pwdb)
    print(pwdb)

