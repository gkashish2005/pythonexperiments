"""Write a python program to find largest between three numbers using functions.
NAME:KASHISH GUPTA 231P081/09"""
print("A program to find largest between three numbers......")
def Largest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
Largest= Largest(num1,num2,num3)
print(f"The Largest number among the numbers {num1},{num2},{num3} is {Largest}.")
print("KASHISH GUPTA 231P081/09")
