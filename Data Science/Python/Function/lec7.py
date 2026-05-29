# Functions in Python

# A function is a block of code that performs a specific task and can be reused multiple times.

# 1. Simple Function
def greet():
    print("Hello, Nitin!")

greet()

# 2. Function with Parameters
def greet(name):
    print("Hello,", name)

greet("Nitin")
greet("Ram")

# 3. Function with Return Value
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# 4. Function with Default Parameter
def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Nitin")

# 5. Function with Multiple Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Nitin", 20)

# 6. Keyword Arguments
def student(name, age):
    print(name, age)

student(age=20, name="Nitin")

# 7. Arbitrary Arguments (*args)
def add(*numbers):
    print(sum(numbers))

add(10, 20)
add(10, 20, 30, 40)

# 8. Keyword Arbitrary Arguments (**kwargs)
def details(**info):
    print(info)

details(name="Nitin", age=20, city="Delhi")

# 9. Lambda Function
square = lambda x: x * x

print(square(5))

# 10. Recursive Function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))