# ###############################
# Linear Search algo -- 
# ###############################

# searching algo which runs on prinicpel of SEQUENTIAL SEARCH 
# where it will travrse through each and every value present in collection 
# one after another to check Key is present or not

# STEPS: 
#   consider a list collection and key to check
#   start comparing val from 0 index to n index
#   after getting val same as key return its index
#   if key is not present the ignore
#   in linear search algo if value is not present then also contorl will compare values by preforming N iteration
#   to overcome this we use binary seach algo

# def linear_search(list, key):
#     for i in range(0,len(list)):
#         if key == list[i]:
#             print(i)
# linear_search([1,2,3,4,5,6],5)

# def linear_search_tup(tup, key):
#     for i in range(len(tup)):
#         if key == tup[i]:
#             print(i)

# linear_search((1, 2, 3, 4, 5, 6), 4)


# def linear_search_string(string, key):
#     for i in range(len(string)):
#         if key == string[i]:
#             print(i)

# linear_search("Hello!", "o")



# ###############################
# Binary Search algo -- 
# ###############################

#   its a searching algo which works on sorted collection  
#   using binary searcg algo its possible to increase efficiency by reducing no of comparison

# steps:
#   consider a collection and key to check
#   init start_idx = 0 and end_idx = len(list)-1 
#   check whether start_idx less than equal to end_idx or not
#   calc_mid idx using (start_idx + end_idx) // 2
#   check whether key == coll[mid_idx]
#   if true return mid pos 
#   elif check key > coll[mid_idx] if true change index + 1
#   start_idx + 1 else check key < coll[mid_idx] if true change end_idx = mid_idx - 1
#   repeat all pts and until u get idx of key

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# def Binary_search(l, key):
#     start_index = 0
#     end_index = len(l) - 1
#     while start_index <= end_index:
#         mid_index = (start_index + end_index) // 2
#         if key == l[mid_index]:
#             return mid_index
#         elif key > l[mid_index]:
#             start_index = mid_index + 1
#         elif key < l[mid_index]:
#             end_index = mid_index - 1
#     return -1

# print(Binary_search(l, 5))  # Output: 4
# print(Binary_search(l, 10))  # Output: -1




# Bubble Sort
#======================================================
# Time: O(n^2)
# Space: O(1)
#======================================================

# sorting algo where each and every val gets swapped based on condition
# to present it or arrange on sorted manner
# in this case we can perfrom n-1 passes where n i nithing but len of input collection 
# in each and evey passses one val will get sorted into respected sorted pos

# A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

# def bubble_sort(arr):
#     n = len(arr)
#     flag = True
#     while flag:
#         flag = False
#         for i in range(1, n):
#             if arr[i-1] > arr[i]:
#                 flag = True
#                 arr[i-1], arr[i] = arr[i], arr[i-1]

# bubble_sort(A)
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
        
#         for j in range(0, n-i-1):
            
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
    
#     return arr



# SIMPLIFIED VERSION
x=[23,6,9,3,10,11]

# for i in range(0, len(x) -1):
#     if  x[i] > x[i+1]:
#         x[i], x[i+1] = x[i+1], x[i]
# print(x) # [6, 9, 3, 10, 11, 23]     

# for i in range(0, len(x) -1):
#     if  x[i] > x[i+1]:
#         x[i], x[i+1] = x[i+1], x[i]
# print(x) # [6, 3, 9, 10, 11, 23]

# for i in range(0, len(x) -1):
#     if  x[i] > x[i+1]:
#         x[i], x[i+1] = x[i+1], x[i]
# print(x) # [3, 6, 9, 10, 11, 23]



# ========================================================

# a = "python apple sql java"
# words = a.split()
# print(words)
# sorted_words = sorted(words)
# sorted_a = " ".join(sorted_words)
# print(sorted_a)

# =========================================================








#======================================================
# Insertion Sort
# Time: O(n^2)
# Space: O(1)
#======================================================

# here current val gets comapared with prev val for sorting 
# STEPS:
#   consider a list collection to sort
#   start pass from 1 as oth pass there will be no prev val for comparison
#   checl weather i is not equal to 0 or notif ture then check weather curr val is less than its prev val
#   if above cond is true then swap both val and decrement val of i by 1
#   repeat steps from 3 to 4 for all passes to et sorted collection


B = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         for j in range(i, 0, -1):
#             if arr[j - 1] > arr[j]:
#                 arr[j - 1], arr[j] = arr[j], arr[j - 1]
#             else:
#                 break
#     return arr

# sorted_B = insertion_sort(B)
# print(sorted_B)


# i=0 --> we cant compare prev val
# a[4] < a[3] --> 2 < 11 --> swap(2,11 --> i++)

# a=[10,7,3,11,2]
a = [ ("akash",1200), ("vijay",10000), ("alex", 8000), ("lakshmi", 6000) ]

i = 1
for passno in range(1,len(a)):
    i = passno
    while i!=0 and a[i] < a[i-1]:
        a[i],a[i-1] = a[i-1],a[i]
        i=i-1
print(a)

for passno in range(1, len(a)):
    i = passno
    while i > 0 and a[i][1] < a[i-1][1]:
        a[i], a[i-1] = a[i-1], a[i]
        i -= 1

print(a)

# output should be like below
# a = [ ("akash",1200),  ("lakshmi", 6000), ("alex", 8000),("vijay",10000) ]