"""Write a python program using Recursive function to calculate sum of a number from 0 to n.
NAME:KASHISH GUPTA 231P081/09"""
def RecursiveSum (n):
     if n==0:
         return 0
     else:
         return n+RecursiveSum(n-1)

n=int(input("Enter the number to calculate the sum of that number from zero:"))
sum= RecursiveSum(n)
print(f"Sum of numbers from 0 to {n} is:",sum)
print("KASHISH GUPTA 231P081/09")
