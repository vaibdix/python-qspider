# 1. Check if the given number is even or odd (take user input)
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


# 2. Check whether the male and female are eligible for wedding (take user input)
gender = input("Enter your gender (male/female): ").lower()
age = int(input("Enter your age: "))
if gender == "male" and age >= 23:
    print("Eligible for wedding.")
elif gender == "female" and age >= 21:
    print("Eligible for wedding.")
else:
    print("Not eligible for wedding.")


# 3. Return uppercase if the character is lowercase, else return the same character (take user input)
char = input("Enter a character: ")
if char.islower():
    print(f"Uppercase version: {char.upper()}")
else:
    print(f"The character remains the same: {char}")


# 4. Return lowercase if the character is uppercase, else return the same character (take user input)
char = input("Enter a character: ")
if char.isupper():
    print(f"Lowercase version: {char.lower()}")
else:
    print(f"The character remains the same: {char}")


# 5. Find the greater value among two numbers
n1 = 34
n2 = 54
if n1 > n2:
    print(f"{n1} is greater than {n2}.")
else:
    print(f"{n2} is greater than {n1}.")


# 6. Check if the given number is even or not, if not even, add 1 to make it even (take user input)
num = int(input("Enter a number: "))
if num % 2 != 0:
    num += 1
    print(f"The number is not even. Adding 1 makes it even: {num}")
else:
    print(f"{num} is already even.")


# 7. Check whether the first character in the given string starts with uppercase, if not, capitalize it
s = "python"
if s[0].islower():
    s = s.capitalize()
print(f"Modified string: {s}")


# 8. Check if the given number is even, if so, reduce it to half; otherwise, make it exponent (take user input)
num = int(input("Enter a number: "))
if num % 2 == 0:
    num //= 2
    print(f"The number is even. Halved number: {num}")
else:
    num **= 2
    print(f"The number is odd. Squared number: {num}")


# 9. Check if a number should be divisible by 3 and 7 (take user input)
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is divisible by both 3 and 7.")
else:
    print(f"{num} is not divisible by both 3 and 7.")


# 10. If the length of the string is even, reverse it; else, convert it to uppercase (take user input)
s = input("Enter a string: ")
if len(s) % 2 == 0:
    reversed_string = s[::-1]
    print(f"Reversed string: {reversed_string}")
else:
    uppercase_string = s.upper()
    print(f"Uppercase string: {uppercase_string}")


# 11. Check if a number is positive or negative (take user input)
num = float(input("Enter a number: "))
if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print("The number is zero.")


# 12. Check if a data is individual or collection data type (take user input)
data = eval(input("Enter a data (can be a single value or a collection): "))
if isinstance(data, (list, tuple, set, dict)):
    print("Collection data type.")
else:
    print("Individual data type.")


# 13. Check whether a specified character is present in the given string
s = "Python"
char = input("Enter a character to search in the string: ")
if char in s:
    print(f"The character '{char}' is present in the string '{s}'.")
else:
    print(f"The character '{char}' is not present in the string '{s}'.")


# 14. Check the length of a dictionary and if it's even, print as it is; else, add an item to make it even
D = {"a": "apple", "b": "ball", "c": "cat"}
if len(D) % 2 == 0:
    print(f"Length of dictionary is even: {D}")
else:
    D["new_key"] = "new_value"
    print(f"Added item to make length even: {D}")


# 15. Check if the given number is greater than 5; if so, convert it to a negative number; else, print the same number
num = float(input("Enter a number: "))
if num > 5:
    num = -num
    print(f"Converted to negative number: {num}")
else:
    print(f"The number remains the same: {num}")


# 16. Check if the given number is smaller than 10; if so, find its exponent; else, print the number as it is
num = float(input("Enter a number: "))
if num < 10:
    exponent = num ** 2
    print(f"Exponent of the number: {exponent}")
else:
    print(f"The number remains the same: {num}")


# 17. Check if the given number is odd; if so, divide it by 2 and print remainder and quotient; else, print it is even (take user input)
num = int(input("Enter a number: "))
if num % 2 != 0:
    quotient = num // 2
    remainder = num % 2
    print(f"The number is odd. Quotient: {quotient}, Remainder: {remainder}")
else:
    print(f"{num} is even.")


# 18. Check if the given character is an alphabet; if so, create a replica of it for 2 times (take user input)
char = input("Enter a character: ")
if char.isalpha():
    replicated_char = char * 2
    print(f"Replicated character: {replicated_char}")
else:
    print("The input is not an alphabet character.")


# 19. Check whether the given number value is divisible by 6 or its cube, else perform left shift by 3 (take user input)
num = int(input("Enter a number: "))
if num % 6 == 0:
    print(f"{num} is divisible by 6.")
elif num % 3 == 0:
    cube = num ** 3
    print(f"The cube of {num} is {cube}.")
else:
    shifted_num = num << 3
    print(f"Left shifted number by 3: {shifted_num}")
