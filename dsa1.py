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

a = "python apple sql java"
words = a.split()
print(words)
sorted_words = sorted(words)
sorted_a = " ".join(sorted_words)
print(sorted_a)

# =========================================================






