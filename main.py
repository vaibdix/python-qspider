# number even or odd

# a = int(input("enter no"))
# if a % 2 != 0:
#     print("Given number is odd", a)
#
# b = int(input("enter no"))
# if b % 2 == 0:
#     print("Given number is Even", b)

# c = int(input("enter score"))
# if c >= 70:
#     print("good luck")

# a=98
# b=67
# if a > b:
#     print("a is greater")
# else:
#     print("b is greater")


# def has_even_length(input_string):
#     return len(input_string) % 2 == 0
#
# Example usage
# string1 = "Hello"


# print(f"String '{string1}' has even length: {has_even_length(string1)}")


# e = int(input("enter to check divisible by 5"))
# if e % 5 == 0:
#     print("divisible by 5")


# p = ["java", "python", "c", "c++", "RUBy", "golang"]
#
# x = input("enter to check availabitity")
# if x in p:
#     print("Available", {x})
#
#
# age = int(input("vote eligiblility test"))
# if age > 18:
#     print("eligible to vote")
#
# pos = int(input("enter pos number"))
# if pos > 0:
#     print("Number is positive")

# upper = input("enter string for upper")
# if upper.isupper():
#     print("entered string is in upper case")

# strr = input("enter string for string validity")
# if strr.isalpha():
#     print("entered string is valid")

# neg = int(input("enter neg number"))
# if neg < 0:
#     print("its negative guys")

# s = "radar"
# if s == s[::-1]:
#     print("palindrome")


# s = "lahari is a good student"
#
# vowel = 'a, e, i, o, u'
# if s[0] not in vowel:
#     print("not a consonent")
# else:
#     print("is vowel")


# val = "Python Coding"
# if a>1 and a<5:
#     print(val)


# a = input("enter ....")
# k = []
# if a%2 == 0:
#     # k=k+[a]
#     k.append(a)
#     print(k)

###############################

# even odd
# if a % 2 == 0:
#     print("Given number is even", a)
# else:
#     print("Given number is even", a)


# char = input("enter char")
#
# if char.islower():
#     print(char.upper())
# else:
#     print(char)

# if char.isupper():
#     print(char.lower())
# else:
#     print(char)


# n1 = 34
# n2 = 54
# if n1 > n2:
#     print(n1)
# else:
#     print(n2)

# s = "python"
# if s[0].isupper():
#     print("not upper")


# TODO 8

# n = input("enter number")
#
# if n%3==0 and n%7==0:
#     print("divisible by 3 and 7")

# n = input("enter string")
# if len(n) % 2 ==0:
#     a = n[::-1]
#     print(a)
# else:
#     print(n.upper())

# n = input("enter number")
# if n>0:
#     print("pos")
# else
#     print("neg")

# data = input("enter data")
# def check_type(data):
#
#     indi = (int, float, str, bool)
#     coll = (list, tuple, set, dict)
#     if isinstance(data, indi):
#         print("part of indi")
#     elif isinstance(data, coll):
#         print("part of coll")
#     else:
#         print("unknown")
#
# check_type(data)


# u = input("enter char")
# s = "python"
#
# if u in s:
#     print("available")
# else:
#     print("not avaibale")


# d = {"a": "apple", "b": "ball", "c": "cat"}
#
# a = len(d)
# if a%2 == 0:
#     print("even", {a})
# else:
#     d.update({"hey":"hey"})

d = int(input("enter number"))
if d > 5:
    print(-abs(d))
else:
    print(d)