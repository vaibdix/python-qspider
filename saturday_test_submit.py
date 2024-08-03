# 1.WAP to replace one string with another string
# s = 'hello world'
# #exp o/p : 'hello Univers


s = 'hello world'
target = 'world'
replacement = 'Universe'

result = ''
i = 0

while i < len(s):
    if s[i:i+len(target)] == target:
        result += replacement
        i += len(target)
    else:
        result += s[i]
        i += 1
print(result)





# 2.WAP to reverse each element in a list,then reverse entire list
# names = ['apple', 'google', 'yahoo', 'walmart']


names = ['apple', 'google', 'yahoo', 'walmart']
reversed_list = [name[::-1] for name in names][::-1]
print("Reverse Each Element in a List, Then Reverse Entire List")
print(reversed_list)




# 3.WAp to sort the list which is mix of both even & odd, the sorted list should have odd numbers first & then even numbers in sorted order
# l = [3, 4, 1, 7, 2, 12, 8, 9, 11, 16, 13]
# o/p #odd ->[1,3,7,9,11,13] even-> [2,4,8,12,16]


l = [3, 4, 1, 7, 2, 12, 8, 9, 11, 16, 13]
odd_numbers = sorted([num for num in l if num % 2 != 0])
even_numbers = sorted([num for num in l if num % 2 == 0])
sorted_list = odd_numbers + even_numbers
print("Sort List with Odd Numbers First, Then Even Numbers")
print("odd ->", odd_numbers)
print("even ->", even_numbers)
print("sorted ->", sorted_list)




#4.WAP to print maximum sum of 3 numbers & minimum sum of 3numbers
numbers = [18,15,20,25, 30,35, 40, 5,10,15]

def find_max_min_sums(numbers):
    numbers.sort()
    min_sum = numbers[0] + numbers[1] + numbers[2]
    max_sum = numbers[-1] + numbers[-2] + numbers[-3]
    return max_sum, min_sum

numbers = [18, 15, 20, 25, 30, 35, 40, 5, 10, 15]

max_sum, min_sum = find_max_min_sums(numbers)
print(f"Maximum sum of 3 numbers: {max_sum}")
print(f"Minimum sum of 3 numbers: {min_sum}")





# 5.WAp to remove duplicates from the list without using empty list or set
# l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5]
# exp o/p :[1,2,3,4,5]

l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5]
i = 0
while i < len(l):
    if l.count(l[i]) > 1:
        l.pop(i)
    else:
        i += 1
print("Remove Duplicates from a List Without Using Empty List or Set")
print(l)  # Output: [1, 2, 3, 4, 5]






# 6.Real time scenario based OOPs
# Requirements:
# ============
# Login into Qspiders class
# username : It should be mail address or phone number
# mail id : It should have 1 @ max of 2 '.' and should ends with .com
# phone number : the length should be 13 including '+'
# pwd: The length should be 8 characters atleast 1uc, 1lc, 1spl, 1digit



from abc import ABC, abstractmethod
import re

class User(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def is_valid(self):
        pass

class EmailUser(User):
    def is_valid(self):
        email_regex = r'^[\w.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$'
        return re.match(email_regex, self.username) is not None

class PhoneUser(User):
    def is_valid(self):
        phone_regex = r'^\+\d{12}$'
        return re.match(phone_regex, self.username) is not None

class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        password = self.password

        if len(password) < 8:
            return False

        if not re.findall(r"[a-z]", password):
            return False

        if not re.findall(r"[A-Z]", password):
            return False

        if not re.findall(r"\d", password):
            return False

        if not re.findall(r"[@$!%*#?&]", password):
            return False

        return True

class Login:
    def __init__(self, username, password):
        if '@' in username:
            self.user = EmailUser(username, password)
        else:
            self.user = PhoneUser(username, password)
        self.password_validator = PasswordValidator(password)

    def login(self):
        if self.user.is_valid() and self.password_validator.is_valid():
            print("Login successful")
        else:
            print("Invalid credentials")

username = "abc@example.com"
password = "Password123!"
login = Login(username, password)
login.login()







# 7..WAP to get given o/p:
# l = ['sun flower', 'lilly flower', 'Marigold flower', 'lion animal',
#     'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
# exp o/p : {'flower': [sun, lilly, marigold, lotus],
# 'animal': [lion, tiger, snake], 'bird': [eagle, pigeon]}


l = ['sun flower', 'lilly flower', 'Marigold flower', 'lion animal',
     'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
result = {}
for item in l:
    word, category = item.split(' ', 1)
    if category in result:
        result[category].append(word)
    else:
        result[category] = [word]
print("Get Flower, Animal, and Bird Categories")
print(result)







# 8.WAP to take 2 list remove repeated elements in both & return a list of unique elements without typecasting to set

def remove_duplicates(l1, l2):
  unique_elements = []
  for num in l1 + l2:
    if num not in unique_elements:
      unique_elements.append(num)
  return unique_elements

l1 = [2, 3, 5, 7, 5, 2]
l2 = [5, 4, 2, 7, 8, 4, 5]

result = remove_duplicates(l1, l2)
print(result)






# 9.WAP to separate vowels & consonants from a string.
# s = 'hello guys good morning welcome to programming class'
# exp o/p :{'vowels': [e,o,u,o,o..], 'conso':[h,l,l]}


s = 'hello guys good morning welcome to programming class'
vowels = 'aeiou'
result = {
    'vowels': [char for char in s if char in vowels],
    'conso': [char for char in s if char.isalpha() and char not in vowels]
}
print("Separate Vowels and Consonants from a String")
print(result)




# 10.WAP to suggest a Student to take which course in QSP/JSP/PYSP
# lst = ['QSP', 'JSP', 'PYSP']
# names = ['Testing', 'Development']

def suggest_course(interest):

  lst = ['QSP', 'JSP', 'PYSP']
  names = ['Testing', 'Development']

  if interest == 'Testing':
    return lst[0]
  elif interest == 'Development':
    return lst[1]
  else:
    return "Invalid interest"

student_interest = 'Testing'
suggested_course = suggest_course(student_interest)
print(suggested_course)
