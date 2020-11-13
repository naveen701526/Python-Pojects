import os
import platform

def clear():
    if 'linux' in platform.system().lower(): 
        os.system( 'clear' )
    elif 'windows' in platform.system().lower():
        os.system('cls')


print('''
  _      ____   _____   _____ _   _    _______     _______ _______ ______ __  __ 
 | |    / __ \ / ____| |_   _| \ | |  / ____\ \   / / ____|__   __|  ____|  \/  |
 | |   | |  | | |  __    | | |  \| | | (___  \ \_/ | (___    | |  | |__  | \  / |
 | |   | |  | | | |_ |   | | | . ` |  \___ \  \   / \___ \   | |  |  __| | |\/| |
 | |___| |__| | |__| |  _| |_| |\  |  ____) |  | |  ____) |  | |  | |____| |  | |
 |______\____/ \_____| |_____|_| \_| |_____/   |_| |_____/   |_|  |______|_|  |_|
                                                                                 
                                                                                 
''')
print('''*****Welcome To Login System*****''')
account = input('''Create an Account? Press 1
                    or 
Login if you have an account! Press 2 \n''')
if account == '1':
    clear()
    print('Welcome to Register Board')
    user_name = input('Enter a username \n')
    email_id = input('Enter a valid email id \n')
    password = input('Enter a password \n')
    confirm_password = input('Repeat password again \n')
    if password != confirm_password:
        cleared = False
        while not cleared:
            print('Password did\'nt match try again!')
            
            password = input('Enter a password \n')
            confirm_password = input('Repeat password again \n')
            if password == confirm_password:
                cleared = True
    f = open("accounts.txt", "a")
    f.write(f'{user_name}\n{email_id}\n{password}\n')
    f.close()
    wanna_log_in = input('Do you want to log in now ! Press "y" or Press "n" to exit!')
    if wanna_log_in == 'y':
        account = '2'


if account == '2':
    exit_loop = False
    while not exit_loop:
        clear()
        
        print('welcome to login board'.title())
        user_name = input('Enter your user name!\n')
        password = input('Enter your password \n')
        f = open("accounts.txt", "r")
        content = f.read()
        if password not in content:
            print('Wrong password try again!!')
        elif user_name not in content:
            print('wrong user id try again!!')
        else:
            print('congratulations you\'re logged in!!')
            exit_loop = True
            f.close()

if account not in ['1', '2']:
    print('enter a valid input!!')

    
