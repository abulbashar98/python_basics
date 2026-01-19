
#******* Function in Python: A function is a reusable block of code that
#*** Performs a specific task
#*** Runs only when it is called
#*** Helps avoid repeating code


#* Basic syntax of a function in python
def function_name(parameters):
    #function body
    return Value

#* Example 1: function with no parameters
def greet():
    print("Hello world!")

# greet()
#> Hello world!



#* Example 2: function with parameters
def greet2(name):
    print("Hello", name)

# greet2("Alice")
#> Hello Alice

# greet2("Bob")
#> Hello Bob



#* Example 3: function with return value
def add(a,b):
    return a+b

result = add(3,5)
# print(result)
#> 8



#* Example 4: function with default parameters
def greet3(name="Bashar"):
    print("Hello", name)

# greet3()
#> Hello Bashar

# greet3("Alice")
#> Hello Alice




#* Example 5: function with multiple return values
def math_operations(a,b):
    return a+b,a*b

sum_value, product_value = math_operations(4,5)
# print(sum_value,product_value)
#> 9 20




#* Example 6: function with keyword arguments
def student(name,age):
    print(name, age)

# student(age=20, name="bob")
#> bob 20
#NOTE: order does not matter while using keyword arguments




#* Example 7: function using *args (variable arguments)
def  total(*numbers):
    return sum(numbers)

# print(total(5,10,15))
#> 30


#* Example 8: function with kwargs(keyword arguments)

def info(**details):
    print(details)

# info(name="Bashar", age=28, nationality="Bangladeshi")
#> {'name': 'Bashar', 'age': 28, 'nationality': 'Bangladeshi'}



#** Simple example of a function:
def calculate_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    else:
        return "C"
    
print(calculate_grade(99))
#> A






