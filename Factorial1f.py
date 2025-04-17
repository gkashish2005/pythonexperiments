"""Write a program in python to compute factorial of a number.
NAME: KASHISH GUPTA 231P081/09"""
num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
print("~A PROGRAM WRITTEN BY KASHISH GUPTA 231P081/09")
