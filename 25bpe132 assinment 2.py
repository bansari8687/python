# Assignment 2: Swap Two Values

def swap_values(a, b):
    a, b = b, a
    return a, b

x = input("Enter first value: ")
y = input("Enter second value: ")

x, y = swap_values(x, y)

print("After Swapping:")
print("First Value:", x)
print("Second Value:", y)
