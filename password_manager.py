
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        key_file.close()

def load_key():
    with  open("key.key", "rb") as file:
        key = file.read()
        file.close()
    return key
master_pwd = input("What is the master password?")


key = load_key() + master_pwd.encode()
fer = Fernet(key)







def view():
    try:
        with open('passwords.txt', 'r') as file:
            for line in file.readlines():
                data = line.rstrip()
                username, password = data.split("|")
                print("Username:", username, "Password:", fer.decrypt(password.encode()).decode())
    except FileNotFoundError:
        print("Password file not found. Create one by adding passwords.")



def add():
    name = input("Account Name")
    pwd = input("password:")

    with open('passwords.txt', 'a') as file:
        file.write(name + "|" + str(fer.encrypt(pwd.encode())))
        file.close()


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode")
