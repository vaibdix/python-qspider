# 1. Check character type without using inbuilt functions:
# char = input("Enter a character: ")
#
# if 'A' <= char <= 'Z':
#     print(f"{char} is uppercase")
# elif 'a' <= char <= 'z':
#     print(f"{char} is lowercase")
# elif '0' <= char <= '9':
#     print(f"{char} is a digit")
# else:
#     print(f"{char} is a special character")


# without using inbuit functions
# char = eval(input("enter the char"))
# if ord('A') <= char <= ord('Z'):
#     print(f"{char} is uppercase")
# elif ord('a') <= char <= ord('z'):
#     print(f"{char} is lowercase")
# elif ord('0') <= char <= ord('9'):
#     print(f"{char} is a digit")
# else:
#     print(f"{char} is a special character")



# 2. Check data type:
# data = input("Enter some data: ")
#
# if isinstance(data, (int, float, complex, bool)):
#     print("The data is an individual data type (int, float, etc.)")
# elif isinstance(data, (str, list, tuple)):
#     print("The data is a sequence (string)")
# else:
#     print("The data is an iterable")






# 3. Handle different data types and operations:
# data = input("Enter some data: ")
#
# if isinstance(data, str):
#     print(f"The length of the string is: {len(data)}")
# elif isinstance(data, list):
#     print(f"Popped element from list: {data.pop()}")
# elif isinstance(data, tuple):
#     print(f"Reversed tuple: {data[::-1]}")
# else:
#     print("Invalid input")







# 4. Categorize age:
# age = int(input("Enter your age: "))
#
# if 0 <= age <= 17:
#     print("You are a child")
# elif 18 <= age <= 30:
#     print("You are an adult")
# elif 31 <= age <= 60:
#     print("You are a man")
# elif 61 <= age <= 100:
#     print("You are a senior citizen")
# else:
#     print("Invalid age")









# 5. Give hike based on experience:
# date_of_joining = int(input("Enter your year of joining: "))
# current_year = 2024
#
# experience = current_year - date_of_joining
#
# if 0 <= experience <= 2:
#     print("No hike")
# elif 3 <= experience <= 5:
#     print("Hike: ₹5000")
# elif 6 <= experience <= 8:
#     print("Hike: ₹7000")
# elif experience >= 9:
#     print("Hike: ₹10000")
# else:
#     print("Invalid input")





# 6. Find smallest value among three numbers:
# a = 65
# b = 34
# c = 76
#
#
# if a > b and a > c:
#     print("a greater")
# elif b>c and b > a:
#     print("b is greater")
# else:
#     print("c is greater")

# print(f"The smallest value among {a}, {b}, {c} is: {smallest}")








# 7. Calculate average marks and print grade:
# marks = []
# for i in range(5):
#     mark = int(input(f"Enter marks for subject {i+1}: "))
#     marks.append(mark)
#
# average = sum(marks) / len(marks)
#
# if 90 <= average <= 100:
#     print("Distinction")
# elif 75 <= average <= 89:
#     print("First class")
# elif 60 <= average <= 74:
#     print("Second class")
# elif 50 <= average <= 59:
#     print("Third class")
# else:
#     print("Fail")


# 8.wap to check the height of the student and make them stand in order

# height = []
# for i in range(3):
#     mark = int(input(f"Height for {i+1}: "))
#     height.append(mark)
#
# print(height.sort())



#9 wap to check eligibility for marriage

# age = int(input("Enter your age: "))
# if age >= 23:
#     print("Eligible for wedding.")
# elif age >= 18:
#     print("Eligible for wedding.")
# else:
#     print("Not eligible for wedding.")


# 10.wap to give discount to customer based on total price(p1+p2+p3)
# 1000 to 3000 price 500 discount and 3001 to 5000 price 1000 discount more than 5001 price
# 1200 discount and less than 1000 price no discount.

# p1 = int(input("enter price for product 1 "))
# p2 = int(input("enter price for product 2 "))
# p3 = int(input("enter price for product 3 "))
# total = p1+p2+p3
# print(total)
#
# if total >=1000 or total <= 3000:
#     print("Discount 500")
# elif total >= 3001 or total <=5000:
#     print("Discount 1000")
# elif total >= 5001:
#     print("Discount 1200")
# else:
#     print("no discount")
#

# color = ["red", "yellow", "green"]
# light = eval(input("enter color"))
# if light == 'red' in color:
#     print("STOP")
# elif light == 'yellow' in color:
#     print("SLOW DOWN")
# else:
#     print("GO")