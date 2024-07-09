
#############################
# FUNCTIONS
#############################

# SYNATAX -- 1
# def function_name(prameter):
#     statement
#     print(statement)
# vn = function_name(argu)





# SYNATAX -- 1
# def function_name(prameter):
#     statement
#     return
# vn = function_name(argu)
# print(vn)




#########################
# EG
#########################
# def even_odd():
#     b=int(input("enter a number"))
#     if b%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd()



# def even_odd(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(10)
# even_odd(7)
# even_odd(9)



# def pal():
#     name=eval(input("enter elements"))
#     if name==name[::-1]:
#         return True
#     else:
#         return False
# a=pal()
# print(a)


# def palindrome(x):
#     if x==x[::-1]:
#         print("its palindrome")
#     else:
#         print("not palindrome")
# palindrome("level")
# palindrome("radar")
# palindrome("alvel")


# x = ["wallmart", "india", "snap", "chat", "fb", "insta", "whatsapp", "group"]
# def check(x):
#     s=[]
#     for i in x:
#         if len(i)%2==0:
#             s.append(i)
#     return s
# print(check(x))

# def operation(a,b):
#     return a+b, a-b, a*b, a/b
#
# print(operation(10,20))


# POSITIONAL ARGUEMNTS
#########################

# def addition(a, b):
#     print(a+b)
# addition(2,4)
# addition(2,3,4)
# addition()


# VARIABLE POSITION ARGUMENTS
#############################

# def add(*args): # here return type is TUPLE
#     print(args) # PACKED FORMAT
#     print(*args) # UNPACKED FORMAT
# add(1,2,3,4,5,6,7, ["sdvsdv","sdsf"])
# add()


# KEYWORD ARGUMENTS
#############################

# def add(a,b):
#     print(a+b)
# add(b=3,a=2) # keyword mentioned so keyword argument



# VARIABEL KEYWORD ARGUEMENT -- return type is {} ie dictionary
#############################

# def name(**kwargs):
#     print(kwargs)
# name(age=21, name="VIKAS", _=["sdvsv"])  # in argu var name should be in alphabets only
# # if noting given for argu will give empty arguments


# variabel postional and keyword arguments *args, **kwargs
   # def Combination(*args, **kwargs):
   #     print(args,kwargs)
   # Combination(11,12,13,a=100,b=200,c=90)
   # Combination()





#1. wap to perform addition and subtraction if "a" is greater than "b" return sum else return difference
# def opera(a,b):
#    if a > b:
#       return a+b
#    else:
#       return a-b
#
# print(opera(4,3))


#2. waf to check string is palindrome or not (take user input)
# def pal(s):
#    return s==s[::-1]
#
# print(pal("radar"))

#3. wap to return length of variable keywords arguments
# def varlen(**kwargs):
#    return len(kwargs)
# print(varlen(a=1,b=2,c=3))

#4. wap to return length of the variable positional arguments
# def varlen2(*kwargs):
#    return len(kwargs)
# print(varlen2(1,2,3,4))

#5. waf to search for character in a given string and return corresponding index

# def pos(string,char):
#    return string.index(char) if char in string else -1
#
# string="coding part is done"
# char = "i"
#
# print(pos(string,char))



# def Check(string,char):
#    l=[]
#    for i,j in enumerate(string):
#       if j==char:
#          l.append((j,i))
#    return l
#
# print(Check(string,"i"))

















#6. wap to squaring of the element in the given list
# l=[1,2,3,4,5]
#
# def sq(x):
#    return [x**2 for x in l]
#
# print(sq(l))

#7. wap to fetch last digit number
# def last(num):
#    return num % 10
# last(321)
# print(last(123))

#8. wap to read 3 numbers from the user,first two numbers should be added and the result of addition should be subtracted by third number
# first = int(input("enter first number"))
# second = int(input("enter second number"))
# third = int(input("enter third number"))
# def calc(first, second, third):
#    tempc = first + second
#    final = tempc - third
#    print(final)

# calc(2,5,6)

#9. wap to find square,cube,square root and cube root of a number
# import math
# def opera(num):
#    print("square", {num*num})
#    print("cube", {num*num*num})
#    print("square_root", {math.sqrt(num)})
#    print("cube_root", {math.pow(num, 1/3)})
#
# print(opera(9))

#10. wap to check the given characters is alphabets or digit or special characters
# def chr_check(num):
#    if num.isalpha():
#       return "alpha"
#    elif num.isdigit():
#       return "number"
#    else:
#       print("is symbol")
# print(chr_check("ac"))


#11. wap to check given iterable is a sequence,if it is a sequence reverse it,if not add one extra element to the iterable
# def check_seq_seqrev(iterable):
#    if isinstance(iterable, (str, tuple, list)):
#       return iterable[::-1]
#    else:
#       return iterable + [None]
#
# print(check_seq_seqrev([1,2,3]))


#12. write a function to print the below output
#should print RCN

# def func(s, n):
#    if n == 1:
#       print(s[1::2])
#
# func("TRACXN",1)

#13. write a function to print the below output
#should print TAX

# func("TRACXN",0)
# def func(s, n):
#    if n == 1:
#       print(s[0::2])
#
# func("TRACXN",1)

# 14.A function take variable number of positional arguments as input. how to check if the arguments are more than 5.
# def check_arf(*args):
#    return len(args) > 5
# print(check_arf(1,2,3,4,5,6))

# 15.WAF to reverse any iterable without using reverse function
# def rev(iterable):
#    return iterable[::-1]
# print(rev("abc"))


# 16.waf to return a dictionary with characters and ascii value pair
# def dic_char_asc(s):
#    return {char: ord(char) for char in s}
# print(dic_char_asc("hello"))

# 17.waf to reverse a iterable if you are passing string or list or tuple else print type of the data
# def check_rev(iterable):
#    if isinstance(iterable, (str, tuple, list)):
#       return iterable[::-1]
#    else:
#       return type(iterable)
# print(check_rev(123))
# print(check_rev("string added"))







###########################
# GENERATORS
###########################


# seq of itera
# 1 by 1


# y=["walmart","sql","fb","python","facebook"]
#
# def so(y):
#     l=[]
#     for i in y:
#         if len(i)%2==0:
#             l.append(i[::-1])
#     yield l
#
# s=so(y)
# print(next(s))







 # GENERATOR EXAMPLES

# wap to generate a+b,a-b,a*b,a/b by taking a and b from user
# def gen(a,b):
#     x = a+b
#     y = a-b
#     z = a*b
#     h = a/b
#     yield x,y,z,h
#
# f = gen(2,4)
# print(next(f))




# wap to generate only values which are divisible by 5

# l=[34,55,60,56,78,90,25,40]
# def so():
#     l2=[]
#     for i in l:
#         if i%5==0:
#             l2.append(i)
#             yield l2
#
# s=so()
# print(next(s))
# print(next(s))
# print(next(s))




# wap to return a iterator which is having square root of values present in the list
# l=[25,36,49,81,9,16]


# import math
# l = [25, 36, 49, 81, 9, 16]
# def square_root_iterator(lst):
#     for num in lst:
#         yield math.sqrt(num)
#
# sqrt_iter = square_root_iterator(l)
# for sqrt_value in sqrt_iter:
#     print(sqrt_value)



# wap to return a iterator having tuples of word and its len pair and typecast into dictionary uisng yield

# l=["instagram","facebook","whatsapp","meta","oracle"]
#
# def word_length_pairs_iterator(lst):
#     for word in lst:
#         yield (word, len(word))
#
# pairs_iter = word_length_pairs_iterator(l)
# result_dict = dict(pairs_iter)
# print(result_dict)



# wap to generate only numeric values in given list
# l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
# def numeric_values(l):
#
#     for i in l:
#         if isinstance(i, (int, float)):
#             yield i
# a=numeric_values(l)
# print(next(a))
# print(next(a))
# print(next(a))


# wap to generate a list if it is individual data type reverse it else return as it is
l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]

# def reverse_individual_types(lst):
#     for item in lst:
#         if isinstance(item, str):
#             yield item[::-1]
#         elif isinstance(item, int):
#             yield int(str(item)[::-1])
#         elif isinstance(item, float):
#             yield float(str(item)[::-1])
#         else:
#             yield item
# reversed_iter = reverse_individual_types(l)
# reversed_list = list(reversed_iter)
# print(reversed_list)



# wap to generate only the string with odd length in given list
# l = ["alexa", "siri", "google", "cortrena"]
# def data(l):
#
#     odd_length_strings = (s for s in l if len(s) % 2 != 0)
#     for string in odd_length_strings:
#         yield(string)
# a=data(l)
# print(next(a))


# wap to create a list of numbers if number are even square it else cube it
l=[2,3,4,5,6,7]

# def oper(l):
#     l2=[]
#     for i in l:
#         if i%2==0:
#             l2.append(i**2)
#             yield l2
# a=oper(l)
# print(next(a))
# print(next(a))
# print(next(a))


# wap to return a list if words is of even length reverse it using generators
# l=["hello","world","python","apple","google","walmart"]
# def rev_even(words):
#     for word in words:
#         if len(word) % 2 == 0:
#             yield word[::-1]
# reversed_even_length_words = list(rev_even(l))
# print(reversed_even_length_words)



# wap to generate the first letter of the word as key and words starting with letter as value using generator
s="python is a programming language and programming is part of life"

def group_words_by_first_letter(s):
    words = s.split()
    grouped = {}

    for word in words:
        key = word[0]
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(word)

    for key, value in grouped.items():
        yield key, value


#         alternative from 472
#       here d is empty dictionary
#         d[i[0]] = [i]
#     else:
#         d[i[0]]+=[i]


s = "python is a programming language and programming is part of life"
result = {key: value for key, value in group_words_by_first_letter(s)}
print([result])

# output:-->[{'p': ['python', 'programming', 'programming', 'part'], 'i': ['is', 'is'], 'a': ['a', 'and'], 'l': ['language', 'life'], 'o': ['of']}]






# wap to generate a list if it is individual data type reverse it else keep it as it is

# def process_elements(a):
#     for element in a:
#         if isinstance(element, (int, float, complex, bool)):
#             yield element[::-1]
#         else:
#             yield element
#
# a = ["good", 45, [1, 2], 78.6, (4, 5), 8 + 7j, {9, 7}, False, {"a": 75}]
# result = list(process_elements(a))
# print(result)






