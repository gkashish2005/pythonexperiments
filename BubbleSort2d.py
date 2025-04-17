"""Write a python program to implement Bubble sort using functions.
NAME:KASHISH GUPTA 231P081/09"""
print("A program on Bubble sort.....")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
                        if arr[j] > arr[j+1]:
                          arr[j], arr[j+1] = arr[j+1], arr[j]
                          swapped = True
        if not swapped:
            break
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
bubble_sort(arr)
print("Sorted array is:", arr)
print("~A PROGRAM WRITTEN BY KASHISH GUPTA 231P081/09")

