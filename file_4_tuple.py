
#******** Tuple in python

#*** Immutable → cannot be changed after creation
#*** Ordered → elements keep their position
#*** Written with parentheses () or commas

T = (1,2,3,4,5,6,7,8,9)


#* T[0] = 999
# print(T)
#> TypeError: 'tuple' object does not support item assignment


#* print(T[3])
#> 4


#*** 🔸 How to change a tuple (indirectly)
# You must convert it to a list, modify it, then convert back.

L = list(T)
L.append(19)
T=tuple(L)
# print(T)
#> (1, 2, 3, 4, 5, 6, 7, 8, 9, 19)



#*** Tuple methods

#* count() ->(count and RETURN occurrence of a value)
occurrence = T.count(19)
# print(occurrence)
#> 1

occurrence_of_unknown = T.count(26)
# print(occurrence_of_unknown)
#> 0


#* index() ->(get index of first occurrence)
# print(T.index(19))
#> 9



