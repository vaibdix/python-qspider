# numpy
import numpy as np
# a = [1,2,3,4]
b = [5,6,7,8]
# n = np.array(a)
# print(n)

a={1:2,5:6,7:8}
n = np.array(a)

print(n.shape)
print(n.dtype)
print(n.size)
print(n.itemsize)
print(n.ndim)

# Creating a 1D array
one_d_array = np.array([1, 2, 3, 4])
print(one_d_array)
print(one_d_array.shape)
print(one_d_array.dtype)
print(one_d_array.size)
print(one_d_array.itemsize)

# Creating a 2D array
# each nested list should have same no of elements
two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print(two_d_array)
print(two_d_array.shape)
print(two_d_array.dtype)
print(two_d_array.size)
print(two_d_array.itemsize)
print(two_d_array.ndim)

# Creating a 3D array
three_d_array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(three_d_array)
print(three_d_array.shape)
print(three_d_array.dtype)
print(three_d_array.size)
print(three_d_array.itemsize)
print(three_d_array.ndim)


x = np.arange(1,17,1)
print(x, 'x')
# converting 1D array to 3D array
# here 2 is row and 2 is column and 4 is depth
three_d_x = x.reshape((2, 2, 4))
print(three_d_x, 'three_d_x')


# converting 1D array to 4D array
# here 2 is row and 2 is column and 2 is depth and 2 is height
four_d_x = x.reshape((2, 2, 2, 2))
print(four_d_x, 'four_d_x')
# clusting the elements in 2D array in above example




# identity matrix
identity_matrix = np.identity(3)
print(identity_matrix, 'identity matrix')

# zero matrix
zero_matrix = np.zeros((3, 3))
print(zero_matrix, 'zero matrix')

# ones matrix
ones_matrix = np.ones((3, 3))
print(ones_matrix, 'ones matrix')

# full matrix
full_matrix = np.full((3, 3), "py")
print(full_matrix, 'full matrix')








# difference between copy and view
# copy() method returns a copy of the array.
# view() method returns a view of the array.
# The copy() method returns a new array.
# The view() method returns a view of the original array.
# The copy() method returns a shallow copy of the array.
# copy
# Creating a 1D array
one_d_array = np.array([1, 2, 3, 4])
one_d_array[0] = 1000
print(one_d_array , "one_d_array -- original", id(one_d_array))
# Creating a copy of an array
copy_array = one_d_array.copy()
print(copy_array , "copy_array -- copy", id(copy_array))

# view
# Creating a 1D array
one_d_array = np.array([1, 2, 3, 4])
one_d_array[0] = 100
print(one_d_array, "one_d_array -- original",  id(one_d_array))
# Creating a view of an array
view_array = one_d_array.view()
print(view_array, "view_array -- view" , id(view_array))





# find position of given arrary
one_d_array = np.array([1, 2, 3, 4, 5, 6, 4, 7, 8, 9])
# Finding the position of an array
position = np.where(one_d_array == 4)
print(position, 'find position')
# Finding the positions of multiple elements in an array
positions = np.where((one_d_array == 4) | (one_d_array == 7))
print(positions, 'positions')




# split
# split() method is used to split an array into multiple sub-arrays.
# The split() method takes two arguments.
# The first argument is the array to be split.
# The second argument is the number of sub-arrays.

one_d_array = np.array([1, 2, 3, 4, 5, 6])
split_array = np.split(one_d_array, 2)
print(split_array, 'split_array')




# scalaroperation
# Scalar operations are performed on each element of an array.
one_d_array = np.array([1, 2, 3, 4, 5, 6])
print(one_d_array + 2, 'scalar addition')
print(one_d_array - 2, 'scalar subtraction')
print(one_d_array * 2, 'scalar multiplication')
print(one_d_array / 2, 'scalar division')



# join array
one_d_array1 = np.array([1, 2, 3])
one_d_array2 = np.array([4, 5, 6])
join_array = np.concatenate((one_d_array1, one_d_array2))
print(join_array, 'concatenate')
join_array = np.hstack((one_d_array1, one_d_array2))
print(join_array, 'hstack')
join_array = np.vstack((one_d_array1, one_d_array2))
print(join_array, 'vstack')
join_array = np.dstack((one_d_array1, one_d_array2))
print(join_array, 'dstak')
join_array = np.column_stack((one_d_array1, one_d_array2))
print(join_array, 'column_stack')



# sort
one_d_array = np.array([4, 2, 1, 3, 5])
sort_array = np.sort(one_d_array)
print(sort_array, 'sort')




# convert 4d array to 1d array
four_d_array = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]])
one_d_array = four_d_array.flatten()
print(one_d_array, 'flatten')





