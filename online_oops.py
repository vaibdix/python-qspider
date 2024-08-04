# CLASS -- class is a blueprint of how a object will behave
#   |   -- class Name should be in PASCAL case and methods name in snake case
#   |
#   | -- DATA OR PROPERTY
#   | -- FUNCTION OR BEHAVIOUR

# OBJECT -- is a instance of a class
# eg     -- Car --> wagoner // wagoner = Car()

# class Atm:
#     # __init__ constructor used to define variables in this method
#     #          code in construct runs as soon as we create object of class
#     def __init__(self):
#         self.pin = ""
#         self.balance = 0
#         self.menu()
#         print("Hello from constructor")
#
#     def menu(self):
#         user_input = input('''
#         Hello how would you like to proceed?
#         1. Enter 1 to create pin
#         2. Enter 2 to deposit
#         3. Enter 3 to withdraw
#         4. Enter 4 to check balance
#         5. Enter 5 to exit
#         ''')
#         if user_input == "1":
#             self.create_pin()
#         elif user_input == "2":
#             self.deposit()
#         elif user_input == "3":
#             self.withdraw()
#         elif user_input == "4":
#             self.check_balance()
#         else:
#             print("exit")
#
#     def create_pin(self):
#         self.pin = input("enter your pin ")
#         print("pin set success")
#
#     def deposit(self):
#         temp = input("enter your pin ")
#         if temp == self.pin:
#             amount = int(input("enter amount "))
#             self.balance = self.balance + amount
#             print("Deposit successful for ", {amount})
#             print("total balance", {self.balance})
#         else:
#             print("Invalid pin")
#
#     def withdraw(self):
#         temp = input("enter your pin ")
#         if temp == self.pin:
#             amount = int(input("enter amount "))
#             if amount <= self.balance:
#                 self.balance = self.balance - amount
#                 print("operation success")
#             else:
#                 print("Low balance")
#         else:
#             print("Invalid pin")
#
#     def check_balance(self):
#         temp = input("enter your pin ")
#         if temp == self.pin:
#             print(self.balance)
#         else:
#             print("Invalid pin")
#
#
# sbi = Atm()
# sbi.deposit()
# sbi.withdraw()
# sbi.check_balance()
# sbi.withdraw()
# sbi.check_balance()


#########################################################
#                   MAGIC METHODS
#########################################################

# class Fraction:
#     def __init__(self, n, d):
#         self.num = n
#         self.den = d
#
#     def __str__(self):
#         return "{}/{}".format(self.num, self.den)
#
#     def __add__(self, other):
#
#         temp_num = self.num * other.den + other.num * self.den
#         temp_den = self.den * other.den
#         return "{}/{}".format(temp_num, temp_den)
#
#     def __sub__(self, other):
#         temp_num = self.num * other.den - other.num * self.den
#         temp_den = self.den * other.den
#         return "{}/{}".format(temp_num, temp_den)
#
#     def __mul__(self, other):
#         temp_num = self.num * other.num
#         temp_den = self.den * other.den
#         return "{}/{}".format(temp_num, temp_den)
#
#     def __truediv__(self, other):
#         temp_num = self.num * other.den
#         temp_den = self.den * other.num
#         return "{}/{}".format(temp_num, temp_den)
#
# x = Fraction(3,4)
# y = Fraction(5,6)
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)


#########################################################
#                   ENCAPSULATION
#########################################################
# __ used to make private var and methods
# and after var are private we can provide access to those var in fxn in specified format eg set_pin as str

# class Atm:
#     # __init__ constructor used to define variables in this method
#     #          code in construct runs as soon as we create object of class
#     def __init__(self):
#         self.__pin = ""
#         self.__balance = 0
#         self.__menu()
#         # print("Hello from constructor")
#
#     def get_pin(self):
#         return self.__pin
#
#     def set_pin(self, new_pin):
#         if isinstance(new_pin, str):
#             self.__pin = new_pin
#             print("Updated Pin")
#         else:
#             print("Not Allowed")
#
#     def __menu(self):
#         # private method cannot be avail by classname.method or obj.meth
#         user_input = input('''
#         Hello how would you like to proceed?
#         1. Enter 1 to create pin
#         2. Enter 2 to deposit
#         3. Enter 3 to withdraw
#         4. Enter 4 to check balance
#         5. Enter 5 to exit
#         ''')
#         if user_input == "1":
#             self.create_pin()
#         elif user_input == "2":
#             self.deposit()
#         elif user_input == "3":
#             self.withdraw()
#         elif user_input == "4":
#             self.check_balance()
#         else:
#             print("exit")
#
#     def create_pin(self):
#         self.__pin = input("enter your pin ")
#         print("pin set success")
#
#     def deposit(self):
#         temp = input("enter your pin ")
#         if temp == self.__pin:
#             amount = int(input("enter amount "))
#             self.__balance = self.__balance + amount
#             print("Deposit successful for ", {amount})
#             print("total balance", {self.__balance})
#         else:
#             print("Invalid pin")
#
#     def withdraw(self):
#         temp = input("enter your pin ")
#         if temp == self.__pin:
#             amount = int(input("enter amount "))
#             if amount <= self.__balance:
#                 self.__balance = self.__balance - amount
#                 print("operation success")
#             else:
#                 print("Low balance")
#         else:
#             print("Invalid pin")
#
#     def check_balance(self):
#         temp = input("enter your pin ")
#         if temp == self.__pin:
#             print(self.__balance)
#         else:
#             print("Invalid pin")


# eg -- private var
####################
# sbi = Atm()
# sbi.__balance = "sdvsfvsv" # this creates temp var but we dont use it so it gives us correct ans
# sbi.deposit()
# sbi.check_balance()

# getter, setter
####################
# sbi = Atm()
# # sbi.set_pin(5.6)
# sbi.set_pin("345")
# print(sbi.get_pin())
# sbi.set_pin(1234)
# print(sbi.get_pin())

################
# SHADY STUFF
################
# sbi = Atm()
# sbi._Atm__balance = "wang"
# sbi.deposit()
# Explain shady -- when we use sbi.__balance = 'adaf' it create temp var which we don't use
#                                                     but under the hood it creates _Class__var = data
#                                                                               ie  _Atm__balance = 0
#                                                     so if we directly edit above line it will update and cause problem
# In python nothing is private






############################################
#           PASS BY REFERENCE
############################################

# class Customer:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# def greet(cust):
#     if cust.gender == "male":
#         print("Hello", cust.name, "sir")
#     else:
#         print("Hello", cust.name, "ma'am")
#
#
# cust = Customer("ankita", "female")
# greet(cust)
# # here we are passing class ka obj as argu to a method




####### Simple Example below for pass by ref

# class Customer:
#     def __init__(self, name):
#         self.name = name
#
# def greet(cust):
#     print("greet", id(cust))
#     cust.name = "nitish"
#     print(cust.name, id(cust))
#
# cust = Customer("Ankita")
# print("obj", id(cust))
# greet(cust)
# # same id for ankita in greet and cust obj
# print(cust.name)
# # even though data for name is changed its ID not changed
# # so obj are mutable like list



#############################################
# COMPOSITION -- IS-A RELATIONSHIP
#############################################
# class Customer:
#     def __init__(self, name, gender, address):
#         self.name = name
#         self.gender = gender
#         self.address = address
#
# class Address:
#     def __init__(self, city, pincode, state):
#         self.city = city
#         self.pincode = pincode
#         self.state = state
#
# add = Address("pune", 411038, "MH")
# cust = Customer("abc", "male", add)
# print(cust.name, cust.gender, cust.address.state)









#############################################
#               INHERITANCE
#############################################

# Inheriting constructor
#########################
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("inside constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera
#
#     def buy(self):
#         print("buying a phone")
#
#     def return_phone(self):
#         print("return phone")
#
# class FeaturedPhone(Phone):
#     pass
# class SmartPhone(Phone):
#     pass
#
# s = SmartPhone(20000, "samsung", "sony")
# print(s.price, s.brand, s.camera)


# Inheriting private members -- child Cannot access pvt mem of parent
#############################
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("inside constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
#
#     def buy(self):
#         print("buying a phone")
#
#     def return_phone(self):
#         print("return phone")
#
# class FeaturedPhone(Phone):
#     pass
# class SmartPhone(Phone):
#     def check(self):
#         print(self.__price)
#
# s = SmartPhone(20000, "samsung", "sony")
# print(s.__price, s.brand, s.camera)



###################################
# Polymorphism
###################################


# Method Overriding
####################
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("inside constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
#
#     def buy(self):
#         print("buying a phone")
#
# class SmartPhone(Phone):
#     def buy(self):
#         print("buying smartphone")
#
# s = SmartPhone(2000,"sony", 12)
# s.buy()


# super
####################
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("inside constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
#
#     def buy(self):
#         print("buying a phone")
#
# class SmartPhone(Phone):
#     def buy(self):
#         print("buying smartphone")
#         super().buy()
#
# s = SmartPhone(2000,"sony", 12)
# s.buy()



# super with constructor
#########################
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("inside constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
#
#     def buy(self):
#         print("buying a phone")
#
#     def return_phone(self):
#         print("return phone")
# class FeaturedPhone(Phone):
#     pass
# class SmartPhone(Phone):
#     def __init__(self, price, brand, camera, os, ram):
#         print("1st")
#         super().__init__(price, brand, camera)
#         self.os = os
#         self.ram = ram
#     def buy(self):
#         print("buying smartphone")
#         super().buy()
#
# s = SmartPhone(2000,"sony", 12, "windows", 12)
# print(s.brand, s.camera, s.os, s.ram )
# s.buy()



# super with constructor -- eg --2
#########################
# class Parent:
#     def __init__(self, num):
#         self.__num = num
#
#     def get_num(self):
#         return self.__num
#
# class Child(Parent):
#     def __init__(self, num, val):
#         super().__init__(num)
#         self.__val = val
#
#     def get_val(self):
#         return self.__val
#
# c = Child(1, 200)
# print(c.get_num(), c.get_val())




# single level inheritance
###########################
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
#     def buy(self):
#         print("buying phone")
#     def return_phone(self):
#         print("returning phone")
#
# class SmartPhone(Phone):
#     pass
#
# s = SmartPhone(1000,"apple", "12")
# print(s.brand, s.camera)
# s.buy()



# Multi level inheritance
###########################
# class Product:
#     def review(self):
#         print("cust review")
# class Phone(Product):
#     def __init__(self, price, brand, camera):
#         print("inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
#     def buy(self):
#         print("buying phone")
#
#
# class SmartPhone(Phone):
#     pass
#
# s = SmartPhone(1000,"apple", "12")
# p = Phone(100, "samsung", 1)
# print(s.brand, s.camera)
# print(p.brand, p.camera)
# s.buy()
# s.review()
# p.review()




# hierarchal inheritance
#############################

# class Phone:
#     def __init__(self, price, brand, camera):
#         print("inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
#     def buy(self):
#         print("buying phone")
#
#
# class SmartPhone(Phone):
#     pass
# class FeaturePhone(Phone):
#     pass
#
# s = SmartPhone(1000,"apple", "12")
# print(s.brand, s.camera)
# s.buy()
# f = FeaturePhone(10,"a", '23')
# f.buy()




# multiple inheritance
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
#     def buy(self):
#         print("buying phone")
#
# class Product:
#     def review(self):
#         print("cust review")
#
# class SmartPhone(Phone, Product):
#     pass
#
#
# s = SmartPhone(1000,"apple", "12")
# print(s.brand, s.camera)
# s.buy()
# s.review()



# MRO -- method resolution order
##################################
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
#     def buy(self):
#         print("buying phone")
#
#
# class Product:
#     def buy(self):
#         print("buying product")
#
# class SmartPhone(Product,Phone): # order will decide which buy will trigger
#     pass
#
# s = SmartPhone(2000, "Apple", 12)
# s.buy()




# MRO -- eg multilevel
##########################
# class A:
#     def m1(self):
#         return 20
# class B(A):
#     def m1(self):
#         return 30
#     def m2(self):
#         return 40
# class C(B):
#     def m2(self):
#         return 20
#
# o1 = A()
# o2 = B()
# o3 = C()
# print(o1.m1() + o3.m1() + o3.m2())



# Below gives ERROR as max recurssion
#####################################
# class A:
#     def m1(self):
#         return 20
# class B(A):
#     def m1(self):
#         val = super().m1() + 30
#         return val
# class C(B):
#     def m1(self):
#         val = self.m1() + 20
#         return val
#
# o3 = C()
# print(o3.m1())





###############################################################################
# Polymorphism -- method overloading  --  same method name but different input
##############################################################################

# method overloading -- cannot be done directly
################################################

# class Geometry:
#     def area(self, radius):
#         return 3.14 * radius * radius
#     def area(self, l, b):
#         return l * b
# o = Geometry()
# print(o.area(4)) # cannot take first area with single input



# method overloading -- can be done by default argument
########################################################
# class Geometry:
#     def area(self, a, b=0):
#         if b == 0:
#             print("Circle", 3.14 * a * a)
#         else:
#             print("rect", a * b)
#
# o = Geometry()
# print(o.area(4))
# print(o.area(4,5))



# Polymorphism -- operator overloading -- Fraction
######################################









############################
#   Abstraction -- hidden
############################
# atleast one abstract method should be in abstract class
# and abstract class should inherit from ABC
# higher level class can force some instructions to lower level class
# cannot make obj of abstract class
# need to add all abstract method in child class or else gives err


# from abc import ABC, abstractmethod
# class BankApp(ABC):
#     def database(self):
#         print("connected to db")
#     @abstractmethod
#     def security(self):
#         pass
#
# class MobileApp(BankApp):
#      def mobile_login(self):
#          print("login mobile")
#      def security(self):
#          print("mobile sec code")
#
# o = MobileApp()
# ml = o.mobile_login()
# s = o.security()
# print(o.database(), ml, s)




# class VTU:
#     exm_date = "23-05-2023"
#     @classmethod
#     def collg1(cls):        #cls = VTU
#         print("waiting for exam date")
#         print(f"exam date is {cls.exm_date}")
#     @classmethod
#     def collg2(cls):        #cls = VTU
#         print("waiting for exam date")
#         print(f"exam date is {cls.exm_date}")
#     @classmethod
#     def collg3(cls):        #cls = VTU
#         print("waiting for exam date")
#         print(f"exam date is {cls.exm_date}")
#
# VTU.exm_date = "25-05-2023"
# VTU.collg1()
# VTU.collg2()










#######################################




class Point:
  def __init__(self, x, y):
    self.x_cod = x
    self.y_cod = y

  def __str__(self):
    return '<{},{}>'.format(self.x_cod, self.y_cod)

  def euclidean_distance(self, other):
    return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5

  def distance_from_origin(self):
    return self.euclidean_distance(Point(0,0))

p1 = Point(0,0)
p2 = Point(2,3)
print(p1.euclidean_distance(p2))
print(p1.distance_from_origin())




