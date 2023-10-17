class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number  # Private attribute for account number
        self.__account_holder_name = account_holder_name  # Private attribute for account holder name
        self.__balance = initial_balance  # Private attribute for account balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient funds for withdrawal.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__balance}")


# Create an instance of the BankAccount class
account = BankAccount("123456789", "John Doe", 1000.0)

# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(1500.0)  # This should result in an "Insufficient funds" message
account.display_balance()