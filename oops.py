# class Room2:
#     Trainers="prabhu"
#     student_count=25
#     subject="Python"
#
# r = Room2()
# print(r)


# without using parenthesis for class
# r1=Room2
# print(r1)

# by using class object
# print(r.Trainers)
# print(r.student_count)
# print(r.subject)
#
# print(Room2())

# this gives doc of the fucntiton
# print(Room2.__dict__)

# using class name
# print(Room2.Trainers)
# print(Room2.student_count)
# print(Room2.subject)
#
#
# class Demo:
#     a = 10
#     b = 20
#
# d = Demo()
# print(d)
#
# d1 = Demo()
# print(d)

# printing demo
# print(d.a)
# print(d1.a)
# print(d.b)
# print(Demo.a)

# After modification
# Demo.a = 45
# print(Demo.a)
# print(d.a)
# print(d1.a)
#
# Demo.a = 56
# print(Demo.a)
# print(d.a)
# print(d1.a)
#
#
# d1.a = "New Data"
# print(d1.a)



###################################
# day 2
###################################

# class Test:
#     def spam(self):
#         print("spam msthod")

# a = Test()
# print(a)
# a.spam()


# calling throught object
# a.spam()

# calling throught classname
# class emp:
#     def Salary(self):
#         amount = 1000
#         print(f'Salary is {amount}')
# e=emp()
# e.Salary()


# class emp:
#     def Salary(self, amount):

#         print(f'Salary is {amount}')
# b=emp()
# b.Salary(5000)


# class Demo:
#     def spam(self, sal):
#         if sal == sal[::-1]:
#             return sal, True
#         else:
#             return sal, False
# d=Demo()
# a=d.spam("mom")
# print(a)



# class Amazon:
#     pname = "watch"
#     price = 500
#     cname = "sunny"
#     cadd = "Pune"
#
#     def order(self):
#         print(f'product name {Amazon.pname}')
#         print(f'price {Amazon.price}')
#         print(f'cust name {Amazon.cname}')
#
#     def Address(self):
#         print(f'cust add {Amazon.cadd}')
# a=Amazon()
# a.order()
# a.Address()

# class Amazon:
#     pname = "watch"
#     price = 500
#     cname = "sunny"
#     cadd = "Pune"

#     def order(self):
#         print(f'product name {self.pname}')
#         print(f'price {Amazon.price}')
#         print(f'cust name {self.cname}')

#     def Address(self):
#         print(f'cust add {self.cadd}')
# b=Amazon()
# Amazon.pname="mobile"
# b.order()
# b.Address()



# WAP to accept list from the user when the method is called,
# first index element in list if it is string then reverse the string
# then replace in same position and return,else if it a integer
# then ask for user to add a element into list and return the updated list,
# else reverse the list and return



# def process_list(lst):
#     if isinstance(lst[0], str):
#         lst[0] = lst[0][::-1]
#     elif isinstance(lst[0], int):
#         num = lst[0]
#         new_elem = int(input(f"Enter an element to add to the list for position {num}: "))
#         lst.insert(num, new_elem)
#     else:
#         lst.reverse()
#     return lst

# process_list()




# WAP to accept list from the user when the method is called,
# first index element in list if it is string then reverse the string
# then replace in same position and return,else if it a integer
# then ask for user to add a element into list and return the updated list,


# def process_list(lst):
#     if len(lst) == 0:
#         return "List is empty"

#     first_element = lst[1]

#     if isinstance(first_element, str):
#         lst[1] = first_element[::-1]
#     elif isinstance(first_element, int):
#         new_element = input("Enter an element to add to the list: ")
#         lst.append(new_element)

#     return lst

# user_list = [3,"abc", 5, 7, 9]
# print("Original list:", user_list)

# updated_list = process_list(user_list)
# print("Updated list:", updated_list)



# class ListProcessor:
#     def process_list(self, lst):
#         if not lst:
#             return "List is empty"
#
#         first_element = lst[1]
#
#         if isinstance(first_element, str):
#             lst[1] = first_element[::-1]
#         elif isinstance(first_element, int):
#             new_element = input("Enter an element to add to the list: ")
#             lst.append(new_element)
#
#         return lst
#
# # Usage
# processor = ListProcessor()
# user_list = [3,"abc", 5, 7, 9]
# print("Original list:", user_list)
#
# updated_list = processor.process_list(user_list)
# print("Updated list:", updated_list)




#######################
# CLASS METHOD
#######################
# When we want to connect main method and decoator method we use classmethod
# classmethod uses decoator as @
# here object points to class name object
# here self is replaced by cls
# here cls points to classname
# in formatting string we can replace election with cls as cls is pointing to classname
# 




# class Election:
#     date="15/07/2021"
#     @classmethod
#     def Area1(cls):
#         print(f'my area electon date is {Election.date}')
#     @classmethod
#     def Area2(cls):
#         x=cls()
#         x.date="16/07/2024"
#         print(f'my area electon date is {x.date}')
#         return x
#     @classmethod
#     def Area3(cls):
#         print(f'my area electon date is {Election.date}')
#
# e=Election()
# Election.date='1/01/2022'     #modification in main class 
# e.date='5/5/2023'
# e.Area1()
# e.Area2()
# e.Area3()




# updateing all values n
# class Election:
#     date="15/07/2021"
#     @classmethod
#     def Area1(cls):
#         print(f'my area electon date is {e.date}')
#     @classmethod
#     def Area2(cls):
#         x=cls()
#         x.date="16/07/2024"
#         print(f'my area electon date is {e.date}')
#         return x
#     @classmethod
#     def Area3(cls):
#         print(f'my area electon date is {e.date}')
#
# e=Election()
# Election.date='1/01/2022'     # modification in main class 
# e.date='5/5/2023'             # moditifcation for entire class with changes to e.date using updated e
# e.Area1()
# e.Area2()
# e.Area3()


# class Election:
#     date="15/07/2021"
#     @classmethod
#     def Area1(cls):
#         x=cls()
#         x.date="16/07/2024"
#         print(f'my area electon date is {x.date}')
#     @classmethod
#     def Area2(cls):
#         x=cls()
#         x.date="17/07/2024"
#         print(f'my area electon date is {x.date}')
#         return x
#     @classmethod
#     def Area3(cls):
#         x=cls()
#         x.date="18/07/2024"
#         print(f'my area electon date is {x.date}')
#
# e=Election()
# Election.date='1/01/2022'     # modification in main class 
# # e.date='5/5/2023'             # moditifcation for entire class with changes to e.date using updated e
# e.Area1()
# e.Area2()
# e.Area3()




######################
# STATIC METHOD
######################
# moditifcation in static method wont work
# static method wont take cls and self 
# static method has @staticmethod decorator

#
# class Day1:
#     a = 1000
#     b = 2000
#
#     @staticmethod
#     def Add(a,b):
#         return a + b
#
#     @staticmethod
#     def Sub(a,b):
#         return a - b
# d = Day1
# Day1.a=300
# Day1.b=400
# print(Day1.Add(2,4))



# class GYM:
#     treadmill = "25KM"
#
#     @classmethod
#     def Men(cls):
#         print(f'weight for treadmill is {cls.treadmill}')    
#     @staticmethod
#     def Women(o):
#         print(o)
#         print(f'weight for treadmill is {o.treadmill}')
# g=GYM()
# print(g)
# g.Women(g)




# write instance method, class method and static method with values updated outside class all three examples
class Example:
    class_variable = 10  # Class variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # Instance variable

    # Instance method
    def instance_method(self):
        return f"Instance method: instance_variable={self.instance_variable}, class_variable={self.class_variable}"

    # Class method
    @classmethod
    def class_method(cls):
        return f"Class method: class_variable={cls.class_variable}"

    # Static method
    @staticmethod
    def static_method():
        return f"Static method: no access to class variables directly"

Example.class_variable = 20

instance1 = Example(100)
instance2 = Example(200)

# Using instance methods
print(instance1.instance_method())  
print(instance2.instance_method()) 
# Using class method
print(Example.class_method()) 
# Using static method
print(Example.static_method())  
