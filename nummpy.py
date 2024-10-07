import numpy as np

original_array = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:")
print(original_array)

copied_array = original_array.copy()
print("\nCopied array:")
print(copied_array)

copied_array[0, 0] = 10
print("\nModified copied array:")
print(copied_array)

print("\nOriginal array after modification:")
print(original_array)

viewed_array = original_array.view()
print("\nViewed array:")
print(viewed_array)

viewed_array[1, 1] = 20
print("\nModified viewed array:")
print(viewed_array)

print("\nOriginal array after modification:")
print(original_array)



import numpy as np

# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Convert 2D array to 3D array
arr_3d = arr_2d[np.newaxis, :, :]

print(arr_3d)