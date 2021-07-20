from account_manager import admin_account_handler
from account_manager.user_account_handler import UserAccountFileHandler
import sys

if __name__ == '__main__':
    admin_name = input('Enter admin name: ')
    password = input('Enter password: ')
    password2 = input('Re-enter password: ')
    if password != password2:
        print('Passwords does not match.')
        sys.exit(0)
    elif not UserAccountFileHandler.pass_strength(password):
        print('Password is not strong enough.')
        sys.exit(0)
    account_number = admin_account_handler.create_account(account_holder_name=admin_name, password=password)
    print(f'Account created successfully with admin ID {account_number}')
