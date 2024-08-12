<p align="center">
  <img src="https://github.com/user-attachments/assets/3c26cc3f-ffae-420a-9e13-abd039159ee2" alt="GIF" width="250"> 
</p>

# BillMe
A Finance Manager System where the user can Input an Income or an Expense, Graph is also available for a clear presentation.

# Features of the BillMe Application

## User Management
- **User Registration**
  - Allows new users to register with a unique username and password.
  - Prevents duplicate registrations by checking for existing usernames.

- **User Login**
  - Authenticates users using their username and password.
  - Provides access to user-specific financial data after successful login.

- **User Balance Management**
  - Updates user balances automatically based on transactions.
  - View current balance within the user menu.

## Transaction Management
- **Add Transactions**
  - Users can add new transactions with details like date, amount, category, and description.
  - Supports both income and expense entries.

- **View Transaction History**
  - Displays transaction history within a specified date range.
  - Provides a summary of total income, total expense, and net savings.
  - Optionally displays a plot of income and expenses over time.

- **CSV File Management**
  - Initializes a CSV file for each user to store transaction data.
  - Appends new transactions to the user’s CSV file.
  - Reads and filters transactions from the CSV file based on a date range.

## Data Visualization
- **Transaction Plotting**
  - Generates a visual plot of income and expense trends over time.
  - Uses Matplotlib to display line graphs for better insights.

## Date Handling
- **Flexible Date Parsing**
  - Accepts multiple date formats during transaction entry.
  - Automatically parses and standardizes dates for consistency.

## User Interface
- **Main Menu Navigation**
  - Offers a simple text-based interface for navigating registration, login, and user operations.
  - Separate menus for registration, login, and user-specific actions.
  
- **Enhanced Transaction Display**
  - Displays transaction history in a visually appealing, tabular format with proper alignment and clear headers.
