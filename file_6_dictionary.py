
#******** Dictionary in Python

#*** Stores key : value pairs
#*** Mutable (can be changed)
#*** Unordered (no index, access by key)
#*** Keys are unique and immutable

d = {"a": 1, "b": 2, "c": 3}

#***** Dictionary Methods

#* clear() ->(removes all items from dictionary)
# d.clear()
# print(d)
#> {}


#* copy() ->(returns a shallow copy of the dictionary)
# d2 = d.copy()
# print(d2)
#> {'a': 1, 'b': 2, 'c': 3}


#* get() ->(returns the value of a key without error if the key does not exist)
# print(d.get("a"))
#> 1
# print(d.get("x"))
#> None
# print(d.get("z", 0))
#> 0


#* items() ->(returns all key value pairs)
# print(d.items())
#> dict_items([('a', 1), ('b', 2), ('c', 3)])


#* keys() ->(returns all keys)
# print(d.keys())
#> dict_keys(['a', 'b', 'c'])


#* pop() -(removes and returns the value of a given key)
# x = d.pop("b")
# print(x)
#> 2
# print(d)
#> {'a': 1, 'c': 3}


#* popitem() ->(removes and returns the value of last inserted key)
# print(d.popitem())
#> ('c', 3)

# print(d)
#> {'a': 1}


#* update() ->(update dictionary with another dictionary or key value pairs)
d.update({"b": 2, "c":3})
# print(d)
#> {'a': 1, 'b': 2, 'c': 3}


#* values() ->(returns all values in dictionary)

dict2 = {"Name": "daniel", "Age": 32, "position": "roommate"}
print(dict2.values())
#> dict_values(['daniel', 32, 'roommate'])