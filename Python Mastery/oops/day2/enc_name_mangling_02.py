class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner 
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError('Invalid amount')
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError('Invalid withdraw amout')
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Invalid balance amount.")

    def __update_balance(self, amount):
        self.__balance = amount
    
    def update_balance_public(self, amount):
        return self.__update_balance(amount)

account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.balance)  # Accessing balance through property
account.withdraw(300)
print(account.balance)
account.balance = 2000  # Using setter to update balance
print(account.balance)

try:
    account.__update_balance(3000)
    # account._BankAccount__update_balance(3000)
except AttributeError as e:
    print(e)

# Calling the private method via a public method
account.update_balance_public(3000)

print(account.balance)