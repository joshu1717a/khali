# ATM Simulation Program  
  
class Account:  
    def __init__(self, account_number, pin, balance=0):  
        self.account_number = account_number  
        self.pin = pin  
        self.balance = balance  
  
    def check_balance(self):  
        return self.balance  
  
    def withdraw(self, amount):  
        if amount > self.balance:  
            print("Insufficient balance")  
        else:  
            self.balance -= amount  
            print(f"Withdrawal successful. New balance: {self.balance}")  
  
    def deposit(self, amount):  
        self.balance += amount  
        print(f"Deposit successful. New balance: {self.balance}")  
  
  
class ATM:  
    def __init__(self):  
        self.accounts = {}  
  
    def create_account(self, account_number, pin, balance=0):  
        self.accounts[account_number] = Account(account_number, pin, balance)  
        print("Account created successfully")  
  
    def authenticate(self, account_number, pin):  
        if account_number in self.accounts:  
            if self.accounts[account_number].pin == pin:  
                return self.accounts[account_number]  
            else:  
                print("Invalid PIN")  
        else:  
            print("Account not found")  
  
    def perform_transaction(self, account, transaction_type, amount):  
        if transaction_type == "withdraw":  
            account.withdraw(amount)  
        elif transaction_type == "deposit":  
            account.deposit(amount)  
        else:  
            print("Invalid transaction type")  
  
  
# Create an ATM object  
atm = ATM()  
  
# Create an account  
atm.create_account("123456", "1234", 1000)  
  
# Authenticate and perform transactions  
account = atm.authenticate("123456", "1234")  
if account:  
    atm.perform_transaction(account, "withdraw", 500)  
    atm.perform_transaction(account, "deposit", 200)  
    print("Account balance:", account.check_balance())  
