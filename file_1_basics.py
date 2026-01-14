msg = "Roll a Dice!"
print(msg)

#*******Python Operators


#*** 1. Logical operators

#* and
x = 10
y = 5
# print(x > y and y < x)
#> true


#* or
# print(x > y or y > x)
#> true


#* not 
is_storm = True
# print(not is_storm)
#> false

is_raining = False
# print(not is_raining)
#> true


#*** 2. Equality operators, Identity operators

#* is
random_list = [1,2,3]
another_list = [1,2,3]
# print(random_list is another_list)
#false (different objects in memory)

#* is not
# print(random_list == another_list)
#> true (different object in memory)

#* ==
# print(random_list == another_list)
#> true

#* "!="
# print(random_list != another_list)
#> false


#*** 3. Arithmetic operator

#* "//" and /

x = 10
y = 3

# print(x / y)
#> 3,3333333...

# print(x // y)
#> 3 (floors the value)

x = -7
y = 2

# print(x / y)
#> -3.5

# print(x // y)
#> -4


#*** 4. Sequencing/Indexing operators

#* s[i]
my_list = [0,1,2,3,4,5]
# print(my_list[2])
#> 2

# print(my_list[5])
#> 5

# print(my_list[9])
#> IndexError: list index out of range 


#* s[start:stop]
# print(my_list[0:4])
#> [0, 1, 2, 3]  (Note: last index value not included)


#* s[start:stop:step]
my_bigger_list = [0,1,2,3,4,5,6,7,8,9]
print(my_bigger_list[0:9:2])
#> [0, 2, 4, 6, 8]



