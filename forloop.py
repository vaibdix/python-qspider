# looping flow control statementa
import shlex

# a = "string data"

# for i in a:
#     print(a)

# li = ["a", "b", "c", "d"]
# for i in li:
#     print(i, end=" ")

# tup = ("asd", "bcd")
# for i in tup:
#     print(i)

# dict = {1:2, 4:"two"}
# for i in dict:
#     print(dict)

# s = ["india", "qsipider", "ear", "fv"]
# for i in s:
#     if i[0] in 'aeiou':
#         print(i)

# y = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in y:
#     if i%2==0:
#         print(i)

# for i in range(120, 144, 1):
#     print(i)
#
# even = []
# odd = []
# for i in range(1, 21, 1):
#     if i % 2 == 0:
#         even.append(i)
# else:
#     odd.append(i)
# print(even)
# print(odd)

# digit = ''
# s = "hello123"
# for i in s:
#     if i.isalpha():
#         print(i)
#     else:
#         print(i.isdigit())


# l = ["vaidegi", "rahul", "shivam", "kapil", "patil"]
# for i in l:
#         print(i[0])

# l=["hello",1,23.4,5+6j,'guys',[2,3,4],True,False]
# for i in l:
#     if isinstance(i, (int, float, bool, complex)):
#         sum=sum+i
# print(sum)






# l1=[]
# l2=[]
# l = "programming day"
# for i in range(len(l)):
#     l1.append(l[i])
#     l2.append(i)
# print(l1)
# print(l2)

# //// or

# print(list(enumerate(l)))

# //// or
# for i in enumerate(l):
#     print(i)

# //// or

# for i,j in enumerate(l):
#     print(i,j)


# a = [1,2,3,4,5,6] #if string mismatch for no of elem then gives only matching elem
# b= [11,12,13,14,15]
# print(tuple(zip(a,b)))
# print(list(zip(a,b)))

# from itertools import  zip_longest # zip_longest is also added here
# a = [1,2,3,4,5,6] #if string mismatch for no of elem then gives only matching elem
# b= [11,12,13,14,15]
# for i in zip_longest(a,b,fillvalue=" filled data"):
#     print(i)
# ///////// OR
# print(list(zip_longest(a,b)))


# s = "india got the independence in the year 1947"
# alpha = []
# digi = []
# space = []
# for i in s:
#
#     if i.isalpha():
#         alpha.append(i)
#     elif i.isdigit():
#         digi.append(i)
#     elif i.isspace():
#         space.append(i)
#     else:
#         print("invalid data")
# print(len(alpha), alpha)
# print(len(digi), digi)
# print(len(space), space)


# dic={}
# s = ("hello world")
# for i in s:
#     dic[i]=ord(i)
# print(dic)



# 9. Create a dictionary from a list and traverse it to reverse the values with even length.
# names = ["apple", "google", "yahoo", "microsoft", "gmail", "walmart"]
# result = {}
#
# for name in names:
#     if len(name) % 2 == 0:
#         result[name] = name
#     else:
#         result[name] = name[::-1]
#
# print(result)


# 10. Print a series of factorials (take user input).
# n = int(input("Enter the number up to which you want the factorial series: "))
# factorials = []
# fact = 1
#
# for i in range(1, n+1):
#     fact *= i
#     factorials.append(fact)
#
# print(factorials)

# to find words in string use split()
# eg
# x="hellow worold sentence"
# count=0
# for i in x.split()
#     count+=1
# print(count)

# 11. Create a dictionary with element and its count pair.
# l = ["yellow", "red", "black", "pink", "orange", "green", "red", "pink", "yellow"]
# count_dict = {}
#
# for item in l:
#     if item in count_dict:
#         count_dict[item] += 1
#     else:
#         count_dict[item] = 1
#
# print(count_dict)


#12. Find the length of the string without using an inbuilt function.
# s = "Never Give Up"
# length = 0
#
# for char in s:
#     length += 1
#
# print(length)


#13. Reverse a string without using an inbuilt function.
# x = "you did it guys"
# reversed_x = ""
#
# for char in x:
#     reversed_x = char + reversed_x
#
# print(reversed_x)

# using inbuilt function do using ::-1 and reversed()


#14. Print alternative characters from a given string.
# s = "hello python"
# alternative_chars = ""
#
# for i in range(len(s)):
#     if i % 2 == 0:
#         alternative_chars += s[i]

# or

# for i in range(0, len(s),2):
#     print(s[i], end=" ")
#
# print(alternative_chars)

# s="tomorrow is weekend and non-veg sepcial"
# d={}
# for i in s.split():
#     a = s[i]
#     print(a)


# s="tomorrow is wwkend an non-verg special"
# d={}
# for i in s.split():
#   d[s.index(i)]=i
# print(d)


#17
# s="sunday"
# dictt = {char: char.upper() for char in s}
# print(dictt)

# other version
# d1={}
# for i in s:
#     d[i] = chr(ord(i)-32)
# print(s)


#18
# l=[89,51,111,77,108,120]
# b = {asci: chr(asci) for asci in l}
# print(b)

#19 create list of charracters and its ASCII value pair
# s='sunday'
# b = [(char, ord(char)) for char in s]
# print(b)

#20 clear() without using inbuilt
# lst = ["hai", "hello", "python", "world", "jingalala"]
# lst*=0
# print(lst)

#21 wap t
# s="today is Tuesday and attending python session"
# d={}
# for i in s.split():
#     if i.endswith("a","e","i","o","u"):
#         d[i] = len(i)
# print(d)


#22 wap to create a dictionary with letter and its word starting with
# s = "hi hello good morning welcome to python session"
# words = s.split()
# letter_dict={}
# for word in words:
#     first_letter = word[0]
#     if first_letter in letter_dict:
#         letter_dict[first_letter].append(word)
#     else:
#         letter_dict[first_letter] = [word]
# print(letter_dict)

#23 wap to create dictionary of charachtera and its indices pair
# s="hello python"
# d={}
# for i, char in enumerate(s):
#     if char in d:
#         d[char].append(i)
#     else:
#         d[char] = [i]
# print(d)

#24
# s="tomorrow is weekend and non-veg special"
# words=s.split()
# b = {word: word[::-1] for word in words}
# print(b)


#25
# l=[1,2,3,4]
# rev=[]
# for i in range(len(l)):
#     rev.insert(0, l[i])
# print(rev)



##################################
# SATURDAY ASSIGNMENT
##################################

#1 WAP to check whether given number is Prime number (Prime number : Any number which is divisible by same number itself)

# n = int(input("Enter a Number: "))
# if n <= 1:
#     is_prime = False
# else:
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break
# print(is_prime)

#2 WAP to print longest word in a sentence
# s = 'life is full of surprises and miracles'
# max_length = 0
# longest_word = ""
# words = s.split()
# for word in words:
#     if len(word) > max_length:
#         max_length = len(word)
#         longest_word = word
# print(f"Its length is: {longest_word}")


# v2
# lenght=''
# for i in s.split():
#     if len(lenght)<len(i):
#         lenght=i
# print(lenght)


#v3
# a=s.split()
# for i in a:
#     break
# print(a, key=len)


#3 WAP to print all the digits in a below list
# l = ['hello', '123', 'Hai', 'python', '345']
# for item in l:
#     for char in item:
#         if ord(char) >= 48 and ord(char) <= 57:
#             print(char, end=" ")

#4 WAP to check the given number is Armstrong or not (Armstrong : Sum of cube of the digits)
# number = int(input("Enter a Number: "))
# number_str = str(number)
# num_digits = len(number_str)
#
# sum_of_cubes = 0
#
# for c in number_str:
#     digit = int(c)
#     cube = digit ** num_digits
#     sum_of_cubes = sum_of_cubes + cube
# if sum_of_cubes == number:
#     print(f"{number} is an Armstrong number.")
# else:
#     print(f"{number} is not an Armstrong number.")
# print(sum_of_cubes)

#V2
# n=370
# x=str(n)
# res = 0
# for i in x:
#     res=res+int(i)**3
# if res == n:
#     print("arms")
# else:
#     print("not arms")


#5.WAP to check given number is perfect number or not (Take user input) (sum of its proper divisor should be equal to original value)

# n = int(input("enter the number"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("perfect")
# else:
#     print("not perfect")



##################################
# MONDAY
##################################

# even = []
# odd = []
# start = 1
# while start <= 20:
#     if start%2==0:
#         even.append(start)
#     else:
#         odd.append(start)
#     start+=1
# print(even)
# print(odd)


# x = [1,2,17,49,50]
# i=0
# sum=0
# while i < len(x):
#     sum = sum + x[i]
#     i+=1
# print(sum)

# start = ord("A")
# while start <= ord("Z")
#     print(chr(start), end="")
#     start+=1

# start = ord("a")
# while start <= ord("a")
#     print(chr(start), end="")
#     start+=1


# big = ord("A")
# small = ord("a")
# while big <= ord("Z") and small <= ord('z'):
#     print(chr(big), chr(small), end="")
#     big+=1
#     small+=1


# a="hello python"
# i=0
# while i < len(a):
#     print(a[i],i, end="")
#     i=i+2


# x = [1, 2, 3+4j, [1,2,3], 'Hi', {1,2}, 3.7, True]
# i=0
# sum=0
# while i < len(x):
#     if isinstance(x[i], (int, float, bool)):
#         print(x[i])
#     i = i + 1


# x = int(input("enter num"))
# i=1
# while i<=0:
#     print(f'{x} * {i} --> {x*i}')
#     i=i+1


# INTERSTING -- gets [1,2,3] out and add without []
# x = [1, 3+8j, "python", [1,2,3], {1,2,3}, {7:9}]
i=0
# tmp=""
# while i < len(x):
#     if isinstance(x[i], list):
#         y=x.pop(3)
#         z = x+y
#         print(z)
#     i=i+1


# y="Hello123"
# while i < len(y):
#     if y[i] in "aeiou":
#         print(y[i], "vowel")
#     else:
#         if y[i].isdigit():
#             print(y[i], "digit")
#     i=i+1



# names="one, two, three, four, five, six"
# i = 0
# xs = names.split(',')
# print(xs)
# while i < len(xs):
#     if i % 2 == 1:
#         print(xs[i][::-1], end=" ")
#     else:
#         print(xs[i], end=" ")
#     i += 1


# 13: Print sum of numbers in a list
# l = [1,2,3,4,5,6,7,8,9]
# total = 0
# i = 0
# while i < len(l):
#     if l[i] % 2 == 0:
#         total += l[i]
#     i += 1
# print("Sum of numbers:", total)


#14: iterate inside a dic and fetch each key seperately
# d={1:20,2:20,"b":"bat","a":"apple",4:60}
# i = 0
# x=list(d.keys())
# while i < len(x):
#     print(x[i], end=" ")
#     i=i+1

#15: wap to fetch only selected values in given list
# s=["bat", "ball", [1,2,3], {4,5}, {90:87}]
# tmp=""
# while i < len(s):
#     if isinstance(s[i], dict):
#         print(s[i])
#     i=i+1


#16: wap to merge 2 char of 2 strings into a single string by taking characters
s1 = "good"
s2 = "well"

merged_string = ""
i, j = 0, 0

while i < len(s1) or j < len(s2):
    if i < len(s1):
        merged_string += s1[i]
        i += 1
    if j < len(s2):
        merged_string += s2[j]
        j += 1

print(merged_string)
