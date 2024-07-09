# comprehension -- list
#               -- set
#               -- dict

##########################
# SYNTAX
##########################
# syntax 1: without if an else condition
# vn[expression for loop condition]

# syntax 2: with if statement
# vn[TSB for loop condition id condition]

# syntax 3: with if else statement
# vn[TSB if condition ELSE FSB for loop condition]


x=[1,2,3,4,5,6]
# res=[]
# for i in x:
#     res.append(i**2)
# print(res)

#---using_comprehension --->
# x = [i**2 for i in x]
# print(x)




# k=[]
# for i in x:
#     if i%2==0:
#         k.append(i)
# print(k)
#---using_comprehension --->
# x = [i for i in x if i%2==0]
# print(x)


#
# z=[]
# for i in x:
#     if i%2==0:
#         z.append(i)
#     else:
#         z.append(i**3)
# print(x)
#---using_comprehension --->
# z = [i if i%2==0 else i**3 for i in x]
# print(z)


##########################
# SET COMPREHENSION
##########################
# syntax 1: without if an else condition
# vn{expression for loop condition}

# syntax 2: with if statement
# vn{TSB for loop condition id condition}

# syntax 3: with if else statement
# vn{TSB if condition ELSE FSB for loop condition}

# #1
# print([i**2 for i in x])
# #2
# print([i for i in x if i%2==0])
# #3
# print({i if i%2==0 else i**3 for i in x})


##########################
# DICT COMPREHENSION
##########################
# syntax 1: without if an else condition
# vn{key:val for loop condition}

# syntax 2: with if statement
# vn{key:val for loop condition id condition}

# syntax 3: with if else statement
# vn{key:val if condition ELSE FSB for loop condition}



#1
# print({i:ord(i) for in x})
# print((i:ord(i) for in x))
#2
# print({i:i if i%2==0 else i**2 for i in x})






# tuple
#1
# print(tuple(i**2 for i in x))
#2
# print(tuple(i for i in x if i%2==0))
#3
# print(tuple(i if i%2==0 else i**3 for i in x))





##########################
# 26 WEDNESDAY
##########################

# 1.wap to check even numbers in a list and return a list containing only even numbers
# l=[2,32,1,52,31,24,56,75]
# print([i for i in l if i%2==0])


# 2.wap to check elements inside the collection are even or odd,
# if it is even make it square of that numbers,if it is odd make it as cube of that numbers

# l=[2,3,5,1,7,2,3]
# print([i**2 if i%2==0 else i**3 for i in l])


#3 wap to return a list containing 10 multiples of 2
# for i in range(1, 11):
#     a = i*2
#     print(a)

# print([i*2 for i in range(1,11)])


#4.wap to return a list containing 10 multiples of given value(take user input)
# inp = int(input("enter the value"))
# for i in range(1, 11):
#     a = i*inp
#     print(a)

# print([i*inp for i in range(1,11)])


# 5.wap to take two lists as input and add that elements and return a single lists
# l1 = eval(input("enter the value"))
# l2 = eval(input("enter another list"))
# print((sum(i) for i in zip(l1, l2)))



# 6.wap to create a list containing tuples having two elements that is index and value of list
# l=["hey","hello","good","evening","python"]
# for i in enumerate(l):
#     print((i))
# print([i for i in enumerate(l)])

# 7.wap to check length of strings present in tuple,if length is even append as it is ,else reverse it and append
l=("hey","hello","good","evenings","python")
l2 = []
# a = len(l)
#
# for i in l:
#     if len(i) % 2 == 0:
#         l2.append(i)
#     else:
#         l2.append(i[::-1])
# print(l2)

print([l if len(i)%2==0 else i[::-1] for i in l])








############################
# COMEPREHENSION
############################

######################################
## SET Comprehension Examples
######################################

# Return a list containing only even numbers:
l = [2, 32, 1, 52, 31, 24, 56, 75]
even_numbers = [x for x in l if x % 2 == 0]
print(even_numbers)

# Modify elements based on even or odd status:
l = [2, 3, 5, 1, 7, 2, 3]
modified_list = [x**2 if x % 2 == 0 else x**3 for x in l]
print(modified_list)

# List containing 10 multiples of 2:
multiples_of_2 = [2 * i for i in range(1, 11)]
print(multiples_of_2)

# List containing 10 multiples of a given value (user input):
n = int(input("Enter a number: "))
multiples_of_n = [n * i for i in range(1, 11)]
print(multiples_of_n)

# Add elements from two lists and return a single list:
l1 = [2, 3, 4, 5]
l2 = [5, 6, 7, 8]
combined_list = [x + y for x, y in zip(l1, l2)]
print(combined_list)

# Create a list of tuples containing index and value pairs:
l = ["hey", "hello", "good", "evening", "python"]
indexed_tuples = [(index, value) for index, value in enumerate(l)]
print(indexed_tuples)

# Modify strings based on their lengths within a tuple:
l = ("hey", "hello", "good", "evenings", "python")
modified_strings = [s if len(s) % 2 == 0 else s[::-1] for s in l]
print(modified_strings)

######################################
## SET Comprehension Examples
######################################
# Remove repeated values and return in a set:

l = [2, 3, 4, 2, 5, 6, 2, 3]
unique_values = {x for x in l}
print(unique_values)

# Create a set by adding elements present at the same index from two lists
l1 = [2, 3, 4, 5, 6, 7, 8, 9]
l2 = [5, 6, 7, 8, 9, 1, 2, 3]
combined_set = {x + y for x, y in zip(l1, l2)}
print(combined_set)

######################################
## Dictionary Comprehension Examples
######################################

# Keys from list, values are square of the key:
l = [2, 3, 4, 1, 6, 2, 7, 8, 4]
square_dict = {x: x**2 for x in l}
print(square_dict)

# Dictionary of values and index pairs:
l = ["google", "apple", "python", "orange"]
index_dict = {word: index for index, word in enumerate(l)}
print(index_dict)

# Dictionary with first character of word as key if word length is even, value is the word:

l = ["google", "apple", "python", "orange"]
even_length_dict = {word[0]: word for word in l if len(word) % 2 == 0}
print(even_length_dict)

# Dictionary where keys are words and values are modified based on their lengths:

l = ["google", "apple", "python", "orange"]
modified_dict = {word: word if len(word) % 2 == 0 else word[::-1] for word in l}
print(modified_dict)

# Dictionary where keys are palindromes and values are reversed versions of non-palindromes:

l = ["banana", "malayalam", "madam", "sir", "mom", "dad"]
palindrome_dict = {word: word if word == word[::-1] else word[::-1] for word in l}
print(palindrome_dict)

