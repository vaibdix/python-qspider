a = [1,2,3,4]

b = 20
c = 0

# DEFAULT EXCEPT BLOCK
try:
    print(a/b)
except:
    print("handled")

# SPECIFIC EXCEPT BLOCK
try:
    print(b/c)
except ZeroDivisionError:
    print("Zero division error is handling")

# GEERIC EXCEPT BLOCK
try:
    print(b/c)
except ZeroDivisionError as e:
    print(e)

# GEERIC EXCEPT BLOCK - 2
try:
    print(b/c)
except Exception as e:
    print(e)
