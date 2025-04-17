"""WAP to perform the following operations on tuple.
1.Create tuple
2.Display tuple
3.Sort the tuple
4.Reverse the tuple
5.Replicate the tuple
6.Find the sum of elements of a tuple
7.Display frequency of an element using count method
Name:Kashish Gupta 09/231P081"""
Tuple=('chai','dosa','vada-pav','samosa-pav','pav-bhaji')#Creation of tuple
print("The created tuple is:",Tuple)#Display tuple
SortedTuple= tuple(sorted(Tuple))#Sort the tuple
print("The sorted tuple is:",SortedTuple)
ReversedTuple=Tuple[::-1]#Reverse the tuple using slicing
print("The reversed tuple is:",ReversedTuple)
ReplicatedTuple=Tuple*3#Replicate the tuple
print("The replicated tuple after 3 times is:",ReplicatedTuple)
count=0
for i in Tuple:#Find the sum of elements of a tuple
    count=count+1
print("The sum of elements in tuple is :",count)
Count=input("Enter the element to find to find its frequency in the tuple:")#Display frequency of an element using count method
print(f"The Frequency of {Count} in the tuple is:",Tuple.count(Count))
print("~A python program by Kashish Gupta 09/231P081")     
