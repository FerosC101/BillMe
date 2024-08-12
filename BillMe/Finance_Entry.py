from datetime import datetime

def get_amount():
    while True:
        try:
            amount = float(input('\t\t\tEnter the amount: '))
            return amount
        except ValueError:
            print('\t\t\tInvalid Input.\n')

def get_category():
    while True:
        category = input('\t\t\tEnter the category (Income/Expense): ').capitalize()
        if category in ['Income', 'Expense']:
            return category
        else:
            print('\t\t\tInvalid Category.')

def get_date(prompt, allow_default=False):
    while True:
        date_str = input(prompt)
        if allow_default and date_str == '':
            return datetime.today().strftime("%d-%m-%Y")
        try:
            return datetime.strptime(date_str, "%d-%m-%Y").strftime("%d-%m-%Y")
        except ValueError:
            print("\t\t\tInvalid date format. Please enter the date in the format %d-%m-%Y")

def get_description():
    return input('\t\t\tEnter the description: ')