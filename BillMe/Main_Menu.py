from User_Management import User, UserManager
from Transaction_Tracker import CSV
from Finance_Entry import *

class MainMenu:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.current_user = None

    def display_menu(self):
        print("               ==============================================================================")
        print("                                                    B i l l M e")
        print("               ==============================================================================")
        while True:
            print('\t\t\t1. Register')
            print('\t\t\t2. Log in')
            print('\t\t\t3. Exit')
            choice = int(input('\t\t\tEnter Choice: '))
            if choice == 1:
                self.register()
            elif choice == 2:
                self.login()
            elif choice == 3:
                break

    def register(self):
        username = input('\t\t\tEnter Username: ')
        password = input('\t\t\tEnter Password: ')
        if self.user_manager.register(username, password):
            print('\n\t\t\tRegistration Successful!\n')
        else:
            print('\n\t\t\tUsername already exists.\n')

    def login(self):
        username = input('\t\t\tEnter Username: ')
        password = input('\t\t\tEnter Password: ')
        if self.user_manager.login(username, password):
            print('\n\t\t\tLogin successful!\n')
            self.current_user = username
            self.user_menu()
        else:
            print('\n\t\t\tInvalid username or password.\n')

    def user_menu(self):
        while True:
            print()
            print("               ==============================================================================")
            print(f"                                            W E L C O M E {self.current_user}")
            print("               ==============================================================================")
            print('\t\t\t1. View Balance')
            print('\t\t\t2. Add Transactions')
            print('\t\t\t3. View Transaction History')
            print('\t\t\t4. Log out')
            choice = int(input('\t\t\tEnter Choice: '))
            if choice == 1:
                self.user_manager.view_balance(self.current_user)
            elif choice == 2:
                CSV.add_transaction(self.current_user)
            elif choice == 3:
                CSV.view_transactions(self.current_user)
            elif choice == 4:
                self.current_user = None
                break

if __name__ == "__main__":
    user_manager = UserManager()
    main_menu = MainMenu(user_manager)
    main_menu.display_menu()
