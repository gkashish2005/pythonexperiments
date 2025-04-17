"""WAP on set to perform following operations
1.Create set
2.Union, intersection, difference, symmetric-difference
3.Change set
4.Remove elements from a set
5.Use pop and clear
6.Display frequency of an element using control statements
Name:Kashish gupta 09/231P081"""
Set1={'jammu-kashmir','south-india','north-india','east-india'}#Create a Set
Set2={'germany','uk','usa','south-india'}
print("The set 1 is:",Set1)
print("The set 2 is:",Set2)
print("The unions of set1 and set2 is:",Set1.union(Set2))#union of the sets
print("The intersection of set1 and set2 is:",Set1.intersection(Set2))#intersection of the sets
print("The difference of set 1 and set 2 is:",Set1.difference(Set2))#difference of the sets
print("The symmetric-difference of the set1 and set2 is:",Set1.symmetric_difference(Set2))#symmetric-difference of the sets
ChangeSet=input("Enter the element you want to change the set with:")
Set1.add(ChangeSet)
print(f"The set1 after changing the set with {ChangeSet} is:",Set1)#Change the set
Set1.clear()#Remove elements from a set using Clear()
print("Set1 after Deleting all the elements from the set is:",Set1)#Remove elements from a set
while Set2:#use pop()
    PoppedElement=Set2.pop()
    print("Popped element from the set 2 is:",PoppedElement)
Set3={'europe','japan','south-korea','north-korea','china'}
print("The set 3 is:",Set3)
Target=input("Enter the target to count its frequency in the Set3:")
Count=0
for i in Set3:
    if i==Target:
        Count=Count+1#Display frequency of an element using control statements
print(f"The frequency of the {Target} in Set3 is :",Count)
print("~A python program by Kashish Gupta 09/231P081")     
