# FUNCTION
#########################
# def pal():
#     name=input("enter elements")
#     if name==name[::-1]:
#         return True
#     else:
#         return False
# a=pal()
# print(a)



# POSITIONAL ARGUEMNTS
#########################

# def addition(a, b):
#     print(a+b)
# addition(2,4)
# # addition(2,3,4)
# # addition()

# POSITIONAL ONLY ARGUEMNTS
#########################

# def addition(a, b, /):
#     print(a+b)
# addition(2,4)
# addition(2,b=4)

# COMBINATION OF POSITON ONLY AND KEYWORD ONLY ARGUMENT
# def addition(a, b,/,*,c,d ):
#     print(a+b+c+d)
# # addition(a=2, b=4)
# addition(2,4, c=5, d=6)

#KEYWORD ONLY ARGUMENT
# def addition(*,a, b, ):
#     print(a+b)
# addition(a=2, b=4)
# addition(2,4)

# KEYWORD ARGUMENTS
#############################

# def add(a,b):
#     print(a+b)
# add(b=3,a=2) # keyword mentioned so keyword argument

# VARIABLE POSITION ARGUMENTS
#############################

# def add(*args): # here return type is TUPLE
#     print(args) # PACKED FORMAT
#     print(*args) # UNPACKED FORMAT
# add(1,2,3,4,5,6,7, ["sdvsdv","sdsf"])
# add()


# VARIABEL KEYWORD ARGUEMENT -- return type is {} ie dictionary
#############################

# def name(**kwargs):
#     print(kwargs)
# name(age=21, name="VIKAS", _=["sdvsv"])  # in argu var name should be in alphabets only
# if noting given for argu will give empty arguments


# variabel postional and keyword arguments *args, **kwargs
# def Combination(*args, **kwargs):
#    print(args,kwargs)
# Combination(11,12,13,a=100,b=200,c=90)
# Combination()



# def ch_check(a):
#     for i in a:
#         if i in 'aeiou':
#             # b=i[1]
#             print(f'Its a vowel', {i}, "next is", )
#         else:
#             print(f'Its a consonent', {i}, "next is", )
# ch_check("asdfghjkol")

#
# y = "Hello123"
# i = 0
#
# while i < len(y):
#     if y[i] in "aeiouAEIOU":
#         if i + 1 < len(y):
#             print(y[i], "vowel", y[i + 1])
#         else:
#             print(y[i], "vowel", "No next element")
#     else:
#         if y[i] not in "aeiouAEIOU":
#             if i - 1 >= 0:
#                 print(y[i], "consonant", y[i - 1])
#             else:
#                 print(y[i], "consonant", "No previous element")
#     i = i + 1




# a="b"
# if a not in "aeiouAEIOU":
#     print(chr(ord(a)+1))
#
# else:
#     print(chr(ord(a)-1))



# def rm_duplicates(input_list):
#     seen = []
#     result = []
#     for item in input_list:
#         if item not in seen:
#             seen.append(item)
#             result.append(item)
#     return result
#
# my_list = [100,300,400,100,500, 700, 700]
# unique_list = rm_duplicates(my_list)
# print(unique_list)




###########################################################################################
#               CLASS QUESTIONS
############################################################################################
# 1. Check if the number is odd and store in a tuple
# number = int(input("Enter a number: "))
# if number % 2 != 0:
#     num_tuple = (number,)
#     print(f"Number is odd and stored in tuple: {num_tuple}")





# 2. Check if last digit is greater than 5 and perform bitwise right shift
# number = int(input("Enter a number: "))
# if number % 10 > 5:
#     result = number >> 2
#     print(f"After right shifting by 2: {result}")





# # 3. Check if number is an integer and odd, then check divisibility by 5
# number = int(input("Enter a number: "))
# if isinstance(number, int) and number % 2 != 0:
#     if number % 5 == 0:
#         print(f"{number} is divisible by 5")





# # 4. Check if the value is an integer and convert to string
# value = input("Enter a value: ")
# if value.isdigit():
#     value_str = str(int(value))
#     print(f"Value as a string: {type(value_str), value_str}")





# # 5. Check if two integers are equal and perform addition
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if num1 == num2:
#     result = num1 + num2
#     print(f"Numbers are equal. Sum: {result}")





# # 6. Check if a character is lowercase and replicate it
# char = input("Enter a character: ")
# if char.islower() and len(char) == 1:
#     print(char * 3)





# # 7. Check if a character is a vowel and print next or previous character
char = input("Enter a character: ")
vowels = 'aeiou'
if char in vowels:
    next_char = chr(ord(char) + 1)
    print(f"Next character: {next_char}")
else:
    prev_char = chr(ord(char) - 1)
    print(f"Previous character: {prev_char}")





# # 8. Check if number is even and convert to negative
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     number = -number
# print(f"Number: {number}")





# # 9. Turn FAN ON or OFF
# status = int(input("Enter 1 to turn FAN ON or 0 to turn FAN OFF: "))
# if status == 1:
#     print("FAN ON")
# else:
#     print("FAN OFF")





# # 10. Display grade based on percentage
# percentage = float(input("Enter percentage: "))
# if percentage > 90:
#     print("Grade: A")
# elif 80 < percentage <= 90:
#     print("Grade: B")
# elif 60 <= percentage <= 80:
#     print("Grade: C")
# else:
#     print("Grade: D")




# # 11. Check if a triangle is possible
# side1 = float(input("Enter the first side: "))
# side2 = float(input("Enter the second side: "))
# side3 = float(input("Enter the third side: "))
# if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
#     print("Triangle is possible")
# else:
#     print("Triangle is not possible")




# # 12. wap to check the given number is digit or not try it both
# with and without using inbuilt function (take user input)

# value = input("Enter a value: ")
# try:
#     int_value = int(value)
#     print("The value is a digit")
# except ValueError:
#     print("The value is not a digit")




# # 13. Check if the first digit is even or odd
# num = 578
# first_digit = int(str(num)[0])
# if first_digit % 2 == 0:
#     print("First digit is even")
# else:
#     print("First digit is odd")





# # 14. Check if number is between 1 and 19
# if it is true square that number or else false cube that number  and display the number.

# number = int(input("Enter a number: "))
# if 1 <= number <= 19:
#     result = number ** 2
# else:
#     result = number ** 3
# print(f"Result: {result}")





# # 15. Check if the student has passed or failed
# marks = int(input("Enter the marks: "))
# if marks > 40:
#     print(f"PASS: {marks}")
# else:
#     print(f"FAIL: {marks}")





# 16. Check if the first character is an alphabet and reverse the string else print the middle character.

#### Good Question
# string = input("Enter a string: ")
# if string[0].isalpha():
#     print(string[::-1])
# else:
#     print(f"Middle character: {string[len(string)//2]}")





# 17. WAP to check whether a given string is less than 3 characters, to print
# the entire string otherwise to print after third positions to the remaining string.

# string = input("Enter a string: ")
# if len(string) < 3:
#     print(string)
# else:
#     print(string[3:])





# # 18. Ravi would like to buy a red pen. The cost of the pen should be 10RS.
# If the pen is available in the shop, he will buy the pen.
# If it is not there he will come out of the shop.
# pen_cost = 10
# pen_available = int(input("Is the pen available? Enter 1 for YES or 0 for NO: "))
# if pen_available == 1:
#     print("Ravi will buy the pen.")
# else:
#     print("Ravi will come out of the shop.")










# # 19..WAP to check length of both string collections are equal or not.
# if both are equal print the concatenation the two strings and display,
# or else if any one of the collection not equal print both the collections with lengths
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# if len(string1) == len(string2):
#     concatenated = string1 + string2
#     print(f"Concatenated string: {concatenated}")
# else:
#     print(f"String 1: {string1}, Length: {len(string1)}")
#     print(f"String 2: {string2}, Length: {len(string2)}")







# # 20. WAP to check whether a given year is a leap year or not.
# if leap year, print leap year or else not a leap year. (take user input)
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")





# 21. wap to accept two integers and check whether they are equal or not if equal
# multiple that value or quotation value display it (take user input)

# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))
# if num1 == num2:
#     result = num1 * num2
#     print(f"Result: {result}")
# else:
#     print(f"Numbers are not equal")




# # 21.wap to accept two integers and check whether they are equal or not
# if equal multiple that value or quotation value display it (take user input)

# x = int(input("enter 1st num"))
# y = int(input("enter 2nd num"))
# if x == y:
#     print(x*y)






# # how to access one clas static method to another class static method when differnt method names
# class Test:
#     @staticmethod
#     def A():
#         print("hi")
#
# class Test2(Test):
#     @staticmethod
#     def B():
#         Test.A()
#         print("Hello")
#
# o = Test2()
# o.B()