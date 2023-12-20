def greet(name):
    print("Hello, " + name + "!")
greet("Alice")

# functions with a return statement

def add(a, b):
    return a + b

result = add(3, 4)
print(result)

#  use the *args syntax to allow a function to accept a variable number of positional arguments.
def sum_all(*args):
    return sum(args)

result = sum_all(1, 2, 3, 4, 5)
print(result)

# lambda functions
multiply = lambda x, y: x * y
result = multiply(3, 4)
print(result)

# recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
