#Don't save passwords to txt file lol
master_pwd = input("What is the master password?")

def view():
    with open('passwords.txt','r') as file:
        for line in file.readlines():
            data = line.rstrip()
        username, password = data.split("|")
        print("Username:",username,"Password:",password)

        file.close()
def add():
    name  =  input("Account Name")
    pwd  = input("password:")

    with open('passwords.txt', 'a') as file:
        file.write(name+"|"+pwd)
        file.close()
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit").lower()
    if mode =='q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode")