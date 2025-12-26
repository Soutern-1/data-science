import numpy as np

numbers = [5,1,3,8,6,7,9,2,4]

array = np.array(numbers)


print(numbers,array)
print("Dimension",array.ndim) 
print("Size",array.size)

# -----------------
# ACCESSING SPECIFIC VALUES OF AN 2D ARRAY

matrix = np.array([[1,2,9,10],[3,4,11,12],[5,6,13,14],[7,8,15,16]])
print("Dimension of matrix",matrix.ndim)

# acessing an item from a 2d list
print("1st row 2nd column item",matrix[0,1])
# printing the whole 2nd row
print("2nd row",matrix[1])

print("part of 2nd row",matrix[1,1:4:2])

# printing a whole column
print("column 2",matrix[0:5,1])

print("column 2",matrix[:,1])

print("row 3",matrix[2,:])

# -----------------
# SORTING AN ARRAY

print("*************************************************")
sorted_nums = np.sort(array)
print(array,sorted_nums)

# Sorting 2d Array

unsorted_2d = [[3,2,4,5],[7,9,8,6],[15,13,14,16],[10,13,12,11]]
unsorted_array = np.array(unsorted_2d)

sorted_array = np.sort(unsorted_array,axis = 1)
print("sorted 2d array (row-wise)",sorted_array)

sorted_array = np.sort(unsorted_array,axis = 0)
print("sorted 2d array (column-wise)",sorted_array)


# -----------------------------------------------------------
print("*************************************************")

# print every third element of a 1d list - linear array
# 5,1,3,8,6,7,9,2,4
print(array[::3])

print(matrix[1:4,1:4])



# -----------------------------------------------------------
print("*************************************************")

linear_array = np.arange(1,50)
print(linear_array)

# making a linear array into a 7x7 array
new_matrix = linear_array.reshape(7,7)
print(new_matrix)

array18 = np.arange(1,19)
print("1x8",array18.reshape(1,18))
print("2x9",array18.reshape(2,9))
print("3x6",array18.reshape(3,6))
print("6x3",array18.reshape(6,3))
print("9x2",array18.reshape(9,2))
print("18x1",array18.reshape(18,1))


# -----------------------------------------------------------
print("*************************************************")

# conditional selection

d1_array = np.array([4,3,5,1,2,7,6,8,9,15,13,16,12,18,19,20,11,14,17,10])
even_array = d1_array[d1_array%2 == 0]
odd_array = d1_array[d1_array%2 != 0]

print(even_array)
print(odd_array)

repeated_array = np.array([1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4])
four_array = repeated_array[repeated_array==4]
print(four_array)
