x = 3

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

x = 10
y = 8

if x > 5 and y > 5:
    print("Both x and y are greater than 5")


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

 # code to be executed as long as the condition is true
count = 0
while count < 5:
    print(count)
    count += 1

for x in range(3):
    for y in range(3):
        print(x, y)

fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "black"]

for fruit, color in zip(fruits, colors):
    print(fruit, color)


squares_generator = (x**2 for x in range(5))
print(list(squares_generator))

