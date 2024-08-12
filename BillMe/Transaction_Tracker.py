import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.parser import parse
from User_Management import UserManager
from Finance_Entry import *

class CSV:
    COLUMNS = ['date', 'amount', 'category', 'description']
    FORMAT = "%d-%m-%Y"

    @classmethod
    def get_csv_file(cls, username):
        return f'{username}_finance_data.csv'
    
    @classmethod
    def initialize_csv(cls, username):
        csv_file = cls.get_csv_file(username)
        if not os.path.exists(csv_file):
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(csv_file, index=False)

    @classmethod
    def add_entry(cls, username, date, amount, category, description):
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }

        csv_file = cls.get_csv_file(username)
        with open(csv_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(new_entry)
            print('\t\t\tEntry added successfully')

        user_manager = UserManager()
        user_manager.update_balance(username, amount, category)

    @classmethod
    def get_transactions(cls, username, start_date, end_date):
        def try_parsing_date(text):
            for fmt in (cls.FORMAT, "%d-%m-%y"):
                try:
                    return datetime.strptime(text, fmt)
                except ValueError:
                    pass
            raise ValueError(f'\t\t\tNo valid date format found for {text}')
        
        csv_file = cls.get_csv_file(username)
        df = pd.read_csv(csv_file)
        df['date'] = df['date'].apply(try_parsing_date)
        start_date = try_parsing_date(start_date)
        end_date = try_parsing_date(end_date)

        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print('\t\t\tNo transactions found in the given range')
        else:
            print(f'\n\t\t\t{"="*62}')
            print(f'\t\t\t{" " * 17}Transactions Summary')
            print(f'\t\t\t{" " * 10}From {start_date} to {end_date}')
            print(f'\t\t\t{"="*62}')
            print(f'\t\t\t| {"Date":^12} | {"Amount":^9} | {"Category":^9} | {"Description":^17} |')
            print(f'\t\t\t{"-"*62}')
            
            for index, row in df.iterrows():
                print(f'\t\t\t| {row["date"].strftime(cls.FORMAT):^12} | Php{row["amount"]:^7.0f} | {row["category"]:^9} | {row["description"]:^17} |')
                print(f'\t\t\t{"-"*62}')
            
            total_income = df[df['category'] == 'Income']['amount'].sum()
            total_expense = df[df['category'] == 'Expense']['amount'].sum()
            
            print(f'\n\t\t\tTotal Income: Php{total_income:.2f}')
            print(f'\t\t\tTotal Expense: Php{total_expense:.2f}')
            print(f'\t\t\tNet Savings: Php{(total_income - total_expense):.2f}\n')
            
        return filtered_df

    @classmethod
    def plot_transactions(cls, df):
        df.set_index("date", inplace=True)
        
        income_df = df[df['category'] == 'Income'].resample("D").sum().reindex(df.index, fill_value=0)
        expense_df = df[df['category'] == 'Expense'].resample("D").sum().reindex(df.index, fill_value=0)
        
        plt.figure(figsize=(10, 5))
        plt.plot(income_df.index, income_df['amount'], label='Income', color='g')
        plt.plot(expense_df.index, expense_df['amount'], label='Expense', color='r')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title('Income and Expense')
        plt.legend()
        plt.grid(True)
        plt.show()

    @classmethod
    def add_transaction(cls, username):
        cls.initialize_csv(username)
        date = get_date('\t\tEnter the date of the transaction (dd-mm-yyyy) or press Enter for today\'s date: ', allow_default=True)
        if date.lower() == '':
            date = datetime.today().strftime(cls.FORMAT)
        amount = get_amount()
        category = get_category()
        description = get_description()
        cls.add_entry(username, date, amount, category, description)

    @classmethod
    def view_transactions(cls, username):
        start_date = get_date('\t\t\tEnter the start date (dd-mm-yyyy): ')
        end_date = get_date('\t\t\tEnter the end date (dd-mm-yyyy): ')
        df = cls.get_transactions(username, start_date, end_date)
        if not df.empty and input('\n\t\t\tDo you want to see a plot? (y/n): ').lower() == 'y':
            cls.plot_transactions(df)
