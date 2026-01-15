
#********* Set in Python

#*** Unordered (no fixed order)
#*** Unindexed (no indexing like s[0])
#*** Mutable as a container (elements can be added/removed)
#*** Contains unique elements only

S = {1,2,3}

#** 🔸 Element-related set methods

#* add() ->(add one element)
S.add(4)
# print(S)
#> {1, 2, 3, 4}

#* clear() ->(remove all elements)
# S.clear()
# print(S)
#> set()

#* copy() ->(Make a copy of the set)
C = S.copy()
# print(C)
#> {1, 2, 3, 4}

#* discard() ->(Remove element, no error if missing)
S.discard(2)
# print(S)
#> {1, 3, 4}

#* pop() ->(remove and return* an arbitary element)
returned_val_from_pop = S.pop()
# print(returned_val_from_pop)
#> 1
#> 1


#*** 🔸 Set operations between multiple sets

A = {1,2,3}
B = {3,4,5}

#* difference() ->(elements in A not in B)
# print(A.difference(B))
#> {1, 2}


#* intersection() ->(common elements)
# print(A.intersection(B))
#> {3}


#* union() ->(all unique elements)
# print(A.union(B))
#> {1, 2, 3, 4, 5}


#* isdisjoint() ->(no common elements? - boolean value)
# print(A.isdisjoint({57,69}))
#> True


#* issubset() ->(is A inside B? - (boolean value))
# print({1,2}.issubset(A))
#> True


#* issuperset() ->(does A contain B? - (boolean value))
# print(A.issuperset({1,2}))
#> True


#* update() ->(add elements from other set)
A.update(B)
print(A)
#> {1, 2, 3, 4, 5}


