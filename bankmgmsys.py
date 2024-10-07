# bank account management system
# classes -> account, customer
# object -> individual account, customer, transactions
# inheritance -> saving account, checking account interit from account
# polymorphism -> deposit, withdraw methods behvea differently for each account type
# encapsulation  -> account balance, customer info hidden from external access

class Customer:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

class Account:
    def __init__(self, customer, balance=0):
        self.__customer = customer
        self.__balance = balance

    def deposit(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")

    def withdraw(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_balance(self):
        return self.__balance

    def get_customer(self):
        return self.__customer

    def set_balance(self, balance):
        self.__balance = balance

class SavingAccount(Account):
    def __init__(self, customer, balance=0, interest_rate=0.02):
        super().__init__(customer, balance)
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            return True
        return False

    def apply_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.set_balance(self.get_balance() + interest)

class CheckingAccount(Account):
    def __init__(self, customer, balance=0, overdraft_limit=100):
        super().__init__(customer, balance)
        self.__overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and (amount <= self.get_balance() + self.__overdraft_limit):
            self.set_balance(self.get_balance() - amount)
            return True
        return False


customer1 = Customer("vinay", "123 pune")
saving_account = SavingAccount(customer1, 500)
checking_account = CheckingAccount(customer1, 200)

print(f"Saving Account Balance: {saving_account.get_balance()}")
print(f"Checking Account Balance: {checking_account.get_balance()}")

saving_account.deposit(150)
print(f"Saving Account Balance after deposit: {saving_account.get_balance()}")

saving_account.withdraw(100)
print(f"Saving Account Balance after withdrawal: {saving_account.get_balance()}")

checking_account.deposit(50)
print(f"Checking Account Balance after deposit: {checking_account.get_balance()}")

checking_account.withdraw(300)
print(f"Checking Account Balance after withdrawal: {checking_account.get_balance()}")

saving_account.apply_interest()
print(f"Saving Account Balance after applying interest: {saving_account.get_balance()}")
