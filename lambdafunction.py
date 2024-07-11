# anonymous fn or lambda function

x = lambda a,b: a+b
print(x(5,6))

a = 57
x=lambda a: f' {a} is even' if a%2==0 else f'{a} its odd'


# write a pg to check if given word is even then print as it is else reverse

# word = "hello"
# x=lambda word: for word in words if word%2==0 f'{word} is even' else f'{word} is odd'
# print(x(word))


#1.wap to find square and cube of given number
f = lambda x: (x**2, x**3)
print(f(5))  # Output: (25, 125)


#2.wap to check the given number is palindrome or not
f = lambda x: str(x) == str(x)[::-1]
print(f(121))  # Output: True

#3.wap to convert negative number to positive number
f = lambda x: x if x > 0 else -x
print(f(-10))  # Output: 10

#4.wap to return the key of a dictionary
#a={"hello":"Sony","How":"are","you":"bye"

# a = {"hello":"Sony","How":"are","you":"bye"}
# f = lambda d, v: list(d.keys())[list(d.values()).index(v)]
# print(f(a, "Sony"))  # Output: 'hello'

#5.wap to check if the number is even or odd
f = lambda x: 'even' if x%2 == 0 else 'odd'
print(f(10))  # Output: even

#6.wap which returns first element of a sequence
f = lambda x: x[0]
print(f([1, 2, 3]))  # Output: 1

#7.wap which returns length of any iterable
f = lambda x: len(x)
print(f('Hello'))  # Output: 5

#8.wap which returns the list of squares of numbers in a list l=[2,3,4,5,6]

l = [2, 3, 4, 5, 6]
f = lambda l: [i**2 for i in l]
print(f(l))  # Output: [4, 9, 16, 25, 36]


#9 wap to check list elements are palindrome or not
l = ["nayana", "kayak", "mom", "school", "bag", "dad"]
f = lambda l: [i for i in l if i == i[::-1]]
print(f(l))  # Output: ['kayak', 'mom', 'dad']

# 10.wap to print the numbers present in a list with their corresponding indices pair
l=[100,200,300,400,500]
f = lambda l: [(i, j) for j, i in enumerate(l)]
print(f(l))

#11.wap to check a data is sequence if it is sequence then return length pair else type pair
data = (1, 2, 3)
f = lambda x: (len(x), type(x)) if isinstance(x, (list, tuple)) else (type(x), len(type(x)))
print(f(data))  # Output: (3, <class 'tuple'>)

# 12.wap to check given number is divisible by 5 and 3
f = lambda x: (x % 5 == 0 and x % 3 == 0)
print(f(15))  # Output: True


# 13.wap to check even or odd,if it is even return square of that value else square root of that value
check_even_odd = lambda x: x**2 if x % 2 == 0 else x**0.5

print(check_even_odd(4))   # Output: 16 (4 squared)
print(check_even_odd(9))   # Output: 3.0 (square root of 9)


# 14.wap to check len of given string ,if length is even return as it is else return reverse of that string
check_length_string = lambda s: s if len(s) % 2 == 0 else s[::-1]

# Test cases
print(check_length_string("python"))   
print(check_length_string("programming"))    

# 15.wap to check length of given string and return value and length in tuple and dictionary
f = lambda x: (x, len(x))
g = lambda x: {x[0]: x[1]}
print(g(f("Hello")))  # Output: {'Hello': 5}
