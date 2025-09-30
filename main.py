#Task -1

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))

num = int(input("Enter a number: "))
result = factorial(num)
print("Facotrial of", num,  "is :", result)



print("......\n" * 3)

#task -2

print("Task 2 from here\n")

import math

num = float(input("Enter a number: "))

sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

print("square root of", num, "is :", sqrt_val)
print("logarithm of", num, "is :", log_val)
print("sine of", num, "is :", sine_val)



print(".....\n" * 5)
print("this is the end of both task, Thanks you!")










