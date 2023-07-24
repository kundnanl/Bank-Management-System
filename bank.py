import random
import mysql.connector

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="bank_db"
)


class Bank:
    def __init__(self):
        self.db_cursor = db_connection.cursor()

    def register_customer(self, name):
        account_number = int(input("Enter your account number: "))
        pin = int(input("Enter your PIN (4 digits): "))

        # Check if the account number is already registered
        select_query = """
        SELECT account_number FROM customers
        WHERE account_number = %s
        """
        values = (account_number,)
        self.db_cursor.execute(select_query, values)
        result = self.db_cursor.fetchone()

        if result is not None:
            print("Account number already exists. Please choose a different account number.")
        else:
            # Insert customer details into the 'customers' table
            insert_query = """
            INSERT INTO customers (name, account_number, pin, balance)
            VALUES (%s, %s, %s, 0.0)
            """
            values = (name, account_number, pin)
            self.db_cursor.execute(insert_query, values)
            db_connection.commit()
            print(f"Customer {name} registered with account number: {account_number}")

    def authenticate_customer(self):
        authenticated = False
        while not authenticated:
            account_number = int(input("Enter your account number: "))
            pin = int(input("Enter your PIN: "))

            # Retrieve customer details from the 'customers' table
            select_query = """
            SELECT * FROM customers
            WHERE account_number = %s AND pin = %s
            """
            values = (account_number, pin)
            self.db_cursor.execute(select_query, values)
            result = self.db_cursor.fetchone()

            if result is not None:
                print("Authentication successful!")
                print(f"Welcome {result[1]}! ")
                authenticated = True
            else:
                print("Authentication failed. Invalid account number or PIN. Please try again.")
        return account_number

    def check_balance(self, account_number):
        select_query = """
        SELECT balance FROM customers
        WHERE account_number = %s
        """
        values = (account_number,)
        self.db_cursor.execute(select_query, values)
        result = self.db_cursor.fetchone()
        if result is not None:
            balance = result[0]
            print(f"Account Balance: {balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        update_query = """
        UPDATE customers
        SET balance = balance + %s
        WHERE account_number = %s
        """
        values = (amount, account_number)
        self.db_cursor.execute(update_query, values)
        db_connection.commit()
        print("Deposit successful.")

    def withdraw(self, account_number, amount):
        update_query = """
        UPDATE customers
        SET balance = balance - %s
        WHERE account_number = %s AND balance >= %s
        """
        values = (amount, account_number, amount)
        self.db_cursor.execute(update_query, values)
        affected_rows = self.db_cursor.rowcount
        db_connection.commit()
        if affected_rows > 0:
            print("Withdrawal successful.")
        else:
            print("Insufficient balance or account not found.")


class Customer:
    def __init__(self, account_number):
        self.account_number = account_number
        self.bank = Bank()

    def check_balance(self):
        self.bank.check_balance(self.account_number)

    def deposit(self, amount):
        self.bank.deposit(self.account_number, amount)

    def withdraw(self, amount):
        self.bank.withdraw(self.account_number, amount)


# Create a customer object
customer = None

# Ask if the user is a new or old customer
is_new_customer = input("Are you a new customer? (y/n): ")

if is_new_customer.lower() == 'y':
    name = input("Enter your name: ")
    bank = Bank()
    bank.register_customer(name)
else:
    authentication = None
    while authentication is None:
        bank = Bank()
        authentication = bank.authenticate_customer()
        if authentication is None:
            print("Please try again.")

    # Create a customer object
    customer = Customer(authentication)

    while True:
        print("Select an option:")
        print("1. Check Balance")
        print("2. Make a Deposit")
        print("3. Make a Withdrawal")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            customer.check_balance()
        elif choice == 2:
            amount = float(input("Enter the deposit amount: "))
            customer.deposit(amount)
        elif choice == 3:
            amount = float(input("Enter the withdrawal amount: "))
            customer.withdraw(amount)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

# Close the database connection
bank.db_cursor.close()
db_connection.close()
