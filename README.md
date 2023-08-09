# Bank Management System

A simple Bank Management System implemented in Python using MySQL for database operations.

## Description

The Bank Management System allows customers to register, authenticate, check balance, deposit, and withdraw funds from their accounts. It utilizes a MySQL database to store customer information and account details.

## Features

- Register new customers with account details
- Authenticate customers with account number and PIN
- Check account balance
- Deposit funds into the account
- Withdraw funds from the account

## Installation

1. Clone the repository:
git clone https://github.com/kundnanl/Bank-Management-System.git

2. Set up the MySQL Database:
- Install MySQL if you haven't already.
- Create a MySQL database named `bank_db`.
- Create a table named `customers` with columns: `id` (INT, auto-increment), `name` (VARCHAR), `account_number` (INT), `pin` (INT), `balance` (FLOAT).

3. Configure MySQL Connection:
- Open the Python script in a text editor.
- Update the database connection details in the `db_connection` object.

4. Run the Python script:
- Open a terminal and navigate to the project directory.
- Run the script using the command: `python script_name.py`

## Usage

1. Launch the script.

2. Choose if you are a new or existing customer:
- If you are a new customer, follow the prompts to register with your name, account number, and PIN.
- If you are an existing customer, authenticate using your account number and PIN.

3. Once authenticated, you can select the following options:
- Check Balance
- Make a Deposit
- Make a Withdrawal
- Exit the system

4. Follow the on-screen prompts to perform the desired action.

## Technologies Used

- Python
- MySQL

## Project Structure

- script_name.py
- README.md

## Roadmap

- Implement user authentication for staff and admin roles.
- Generate transaction reports and account summaries.
- Implement fund transfer functionality.

## Contributing

Contributions are welcome! Please follow the guidelines in CONTRIBUTING.md for bug reports, feature requests, and code contributions.
