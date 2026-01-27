class bank:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}. New balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: {amount}. New balance: {self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def get_balance(self):
        return f"Current balance: {self.balance}"

    def get_account_info(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"
    
# Example usage
account1 = bank("123456789", "Sarthak", 1000)
print(account1.get_account_info())
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.get_balance())


account2 = bank("987654321", "Sahil")
print(account2.get_account_info())
print(account2.deposit(300))
print(account2.withdraw(100))
print(account2.get_balance())

account3 = bank("555666777", "Sagar", 1500)
print(account3.get_account_info())  
print(account3.withdraw(2000))
print(account3.deposit(-100))