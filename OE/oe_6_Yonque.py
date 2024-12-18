#oe_6
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("Error: Balance cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            print("Error: Insufficient funds or invalid withdrawal amount.")

    def display_account_info(self):
        print("Account Number:", self._account_number)
        print("Current Balance:", self._balance)

    def _display_balance(self):  
        print("Current Balance:", self._balance)

account = BankAccount("123456789", 1000.0)

account.deposit(500.0)
print("After deposit:")
account.display_account_info()
account.withdraw(200.0)
print("After withdrawal:")
account.display_account_info()
account.set_balance(-500.0)
account._display_balance()