import os
import csv

class User:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance

    def to_dict(self):
        return {
            'username' : self.username,
            'password' : self.password,
            'balance' : self.balance
        }
    
class UserManager:
    def __init__(self, user_file='/users.csv'):
        self.user_file = user_file
        self.users = self.load_users()

    def load_users(self):
        users = {}
        if os.path.exists(self.user_file):
            with open(self.user_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    username = row['username']
                    users[username] = {
                        'username' : row['username'],
                        'password' : row['password'],
                        'balance' : float(row['balance'])
                    }
        return users
            
    def save_users(self):
        with open(self.user_file, 'w', newline='') as file:
            fieldnames = ['username', 'password', 'balance']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.users.values():
                writer.writerow(user)
    
    def register(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password).to_dict()
        self.save_users()
        return True
    
    def login(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return True
        return False
    
    def validate_info(self, username, password):
        if username < 4:
            print('\t\t\tUsername must be at least 4 characters long')
            return False
        if password < 6:
            print('\t\t\tPassword must be at least 6 characters long')
            return False
        return True
    
    def get_balance(self, username):
        if username in self.users:
            return self.users[username]['balance']
        return None
    
    def update_balance(self, username, amount, category):
        if username in self.users:
            if category == 'Income':
                self.users[username]['balance'] += amount
            elif category == 'Expense':
                self.users[username]['balance'] -= amount
            self.save_users()

    def view_balance(self, username):
        balance = self.get_balance(username)
        print()
        print("               ==============================================================================")
        print("                                                    B A L A N C E")
        print("               ==============================================================================")
        print(f'\n\t\t\tCurrent Balance: Php{balance:.2f}\n')
        print()
    

