# #1 Check if a number is odd (take user input)
# num = int(input("Enter a number: "))
# if num % 2 != 0:
#     print(f"{num} is odd.")


# #2 Check if a number is even (take user input)
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is even.")


# #3 Check if a student has scored 70% and print "good luck" (take user input)
# score = float(input("Enter the student's score: "))
# if score >= 70:
#     print("Good luck!")


# #4 Check which number is greater using if condition
# a = 98
# b = 67
# if a > b:
#     print(f"{a} is greater than {b}.")


# #5 Check if a given string has even length of characters
# s = "hey guys you all are Osam"
# if len(s) % 2 == 0:
#     print("The string has even length of characters.")


# #6 Check if a given number is divisible by 5 (take user input)
# num = int(input("Enter a number: "))
# if num % 5 == 0:
#     print(f"{num} is divisible by 5.")


# #7 Check if a given programming language is present in the list
# p = ["java", "python", "c", "c++", "RUBy", "golang"]
# search = input("Enter a programming language: ").lower()
# if search in p:
#     print(f"{search} is present in the list.")


# #8 Check eligibility to vote (take user input as age)
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")


# #9 Check if a given number is positive (take user input)
# num = float(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is positive.")


# #10 Check if a given string is palindrome (take user input)
# s = input("Enter a string: ")
# if s == s[::-1]:
#     print(f"{s} is a palindrome.")


# #11 Check if the first letter in a given string is consonant
# s = "Lahari is a good student"
# first_letter = s[0].lower()
# if first_letter.isalpha() and first_letter not in 'aeiou':
#     print(f"The first letter '{s[0]}' is a consonant.")


# #12 Check if the given string is uppercase or not (take user input)
# s = input("Enter a string: ")
# if s.isupper():
#     print(f"{s} is uppercase.")


# #13 Check if the given value is a string (take user input)
# value = input("Enter a value: ")
# if isinstance(value, str):
#     print(f"{value} is a string.")


# #14 Display "Python Coding" if the number is greater than 1 and less than 5 (take user input)
# num = float(input("Enter a number: "))
# if 1 < num < 5:
#     print("Python Coding")


# #15 Check whether a given number is negative and print "its negative guys"
# num = float(input("Enter a number: "))
# if num < 0:
#     print("Its negative guys")


# #16 Check whether given input is divisible by 2 and 6, convert to complex number if true (take user input)
# num = int(input("Enter a number: "))
# if num % 2 == 0 and num % 6 == 0:
#     num = complex(num)
#     print(f"The number after converting to complex: {num}")


# #17 Check whether the given number is even or not, store the value inside the list (take user input)
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     even_numbers = [num]
#     print(f"The even number {num} is stored in the list: {even_numbers}")

#18 Not available

#19 Check whether a given value is divisible by 5 and 7, display the square of the value if divisible (take user input)
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 7 == 0:
    square = num ** 2
    print(f"The square of {num} is {square}.")
# input 35


#20 Check whether a given value is present between 45 and 200, divisible by 4 and 5, display ASCII characters (take user input)
num = int(input("Enter a number: "))
if 45 < num < 200 and num % 4 == 0 and num % 5 == 0:
    print(f"The ASCII character of {num}: {chr(num)}")
# input 80 - p

# #21 Check if a string contains a substring (take user input for both string and substring)
string = input("Enter a string: ")
substring = input("Enter a substring to search: ")
if substring in string:
    print(f"The substring '{substring}' is present in the string '{string}'.")



# #22 Check whether a character is in the alphabet or not, store in a dictionary (key as character, value as ASCII) (take user input)
character = input("Enter a character: ")
if character.isalpha():
    ascii_value = ord(character)
    char_dict = {character: ascii_value}
    print(f"The character '{character}' with ASCII value {ascii_value} is stored in the dictionary: {char_dict}")


# #23 Check whether a character is uppercase or not, convert to lowercase and store in a dictionary (character as key, ASCII as value) (take user input)
char = input("Enter a character: ")
if char.isupper():
    lowercase_char = char.lower()
    ascii_value = ord(char)
    char_dict = {lowercase_char: ascii_value}
    print(f"The uppercase character '{char}' with ASCII value {ascii_value} converted to lowercase '{lowercase_char}' is stored in the dictionary: {char_dict}")
