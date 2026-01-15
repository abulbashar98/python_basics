
#******* list in python

#*** Mutable → can be changed
#*** Ordered → elements keep their position
#*** Written with square brackets []

A = [1,2,3,4,5,6] 

#***** Methods in a list

#* append() ->(add one element at the end)
A.append(10)
# print(A)
#> [1, 2, 3, 4, 5, 6, 10]

#* clear() ->(remove all elements)
# A.clear()
# print(A)
#> []

#* copy() ->(create a shallow copy)
B = A.copy()
# print(B)
#> [1, 2, 3, 4, 5, 6, 10]
# Note: B is a separate list with same elements (in memory)
B.clear()
# print(B)
#> []

# print(A)
#> [1, 2, 3, 4, 5, 6, 10]


#* count() ->(returns count of occurrence of a value)
# A.append(10)
# print(A)
#> [1, 2, 3, 4, 5, 6, 10,10]

occurrence = A.count(10)
# print(occurrence)
#> 2


#* extend() ->(add elements from another list)
C = [11,12]
A.extend(C)
# print(A)
#> [1, 2, 3, 4, 5, 6, 10, 11, 12]

A.extend([13,14])
# print(A)
#> [1, 2, 3, 4, 5, 6, 10, 11, 12,13,14]


#* index() ->(get index of first occurrence)
# print(A.index(11))
#> 7


#* insert() ->(insert at a specific position)
A.insert(0,999)
# print(A)
#> [999, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14]


#* pop() ->(remove and RETURN an element)
value = A.pop()
# print(value)
#> 14

# print(A)
#> [999, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13]


#* remove() ->(remove first matching value)
A.remove(999)
# print(A)
#> [1, 2, 3, 4, 5, 6, 10, 11, 12, 13]

#* reverse() ->(reverse the list)
A.reverse()
# print(A)
#> [13, 12, 11, 10, 6, 5, 4, 3, 2, 1]


#* sort() ->(sort the list)
A.sort()
print(A)
#> [1, 2, 3, 4, 5, 6, 10, 11, 12, 13]

