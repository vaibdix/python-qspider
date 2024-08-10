# class Bank:
#     def __init__(self, name, ifsc, location):
#         self.name = name
#         self.ifsc = ifsc
#         self.location = location
#         self.balance = 0
#
#     def deposit(self, amount):
#         if amount + self.balance > 200000:
#             raise ValueError("Cannot deposit 2 lakh and above")
#         self.balance += amount
#         print(f"Deposited {amount}. Current balance: {self.balance}")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient funds.")
#         self.balance -= amount
#         print(f"Withdrew {amount}. Current balance: {self.balance}")
#
#     def get_balance(self):
#         return self.balance
#
# bank = Bank(name="ICICI BANK", ifsc="IFSCODE", location="New York City")
#
# try:
#     bank.deposit(100000)
#     bank.withdraw(25000)
#     bank.deposit(75000)
#     bank.deposit(150000)
# except ValueError as e:
#     print(e)
# bank.deposit(150000)



#########################
# IMP
########################

class Test:
    @staticmethod
    def demo():
        print("demo")


class Test2(Test):
    @staticmethod
    def demo2():
        super(Test2,Test2).demo()
        print("demo2")

Test2.demo2()















