import os
import json
import random
import string

PWDB_FILENAME = 'pwdb.json'
SALT_LENGTH = 5
VALID_CHAR = string.ascii_letters + string.digits + string.punctuation


def get_credentials():
    username = input('Type the username: ')
    password = input('Type the password: ')
    return username, password

def add_user(user, password, pwdb):
    salt = get_random_salt()
    pwdb[user] = (salt, pwhash(salt+password))
    write_pwdb(pwdb)
    return

def wrong_pwd_or_no_user(user, password, pwdb):
    print('Username does not exist or the password is wrong.')
    answer = input('Add user to the db? ')
    if answer == 'y':
        if user in pwdb:
            pass
        else:
            add_user(user, password, pwdb)
    return

def authenticate(user, password, pwdb):
    if user in pwdb:
        salt, hash_ = pwdb[user]
        if pwhash(salt+password) == hash_:
            print('Successfully authenticated!')
        else:
            wrong_pwd_or_no_user(user, password, pwdb)
    else:
        wrong_pwd_or_no_user(user, password, pwdb)
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
    #print(pwdb)

