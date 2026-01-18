
#****** Python offers Matlab-like indexing method for lists/tuples, making list indexing and slicing very convenient.

a = [1,2,3,4,5,6,7,8,9]

#* indexing
b = a[2]
# print(b)
#> 3

#* slicing-(NOTE: Last index element not included)
c = a[1:5]
# print(c)
#> [2, 3, 4, 5]

#* Negative indexing-(returns the element at the last index)
d = a[-1]
# print(d)
#> 9

#* slicing with index and steps. NOTE: returns all values except last index 
e = a[2:8:2]
# print(e)
#> [3,5,7]

#* slicing from given first index to last index, all values
f = a[4:]
# print(f)
#> [5, 6, 7, 8, 9]

#* slicing with steps only. Slices 1st to last index. All values
g = a[::2]
# print(g)
#> [1, 3, 5, 7, 9]

#* slicing with steps and given reps
h = a[::2][:4]
# print(h)
#> [1, 3, 5, 7]

#* reverse slicing of all values
k = a[::-1]
# print(k)
#> [9, 8, 7, 6, 5, 4, 3, 2, 1]

#* reverse slicing with given indexes
j = a[3:1:-1]
# print(j)
#> [4, 3]

#* slicing with steps until given negative index
q = a[1:-3:2]
# print(q)
[2, 4, 6]
