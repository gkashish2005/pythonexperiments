"""WAP in python to implement following list operations:
1.Create a list
2.Display list
3.Find length of list
4.Check Element is in list or not using control statements
5.Concatenating lists in python
6.Replacing list elements with new one in python
7.Deleting elements from list in python
8.Create nested lists and display elements of nested list
Name:Kashish Gupta 09/231P081"""
list=["C","Java","Python","Javascript","Sql","Cybersecurity","Ethical-hacking"]#create a list
print("List is:",list)#Display the created list
print("Length of the list is:",len(list))#Find length of list
print("Check Element is in list or not:")#Check Element is in list or not using control statements
CheckElement=input("Enter element to check in list:")
if CheckElement in list:
    print(f"{CheckElement} is in the list")
else:
    print(f"{CheckElement} is not in the list")
AddList=["Cloud-computing","Artificial-Intelligence","Data-Scientist","Data-Analyst","Development"]
print("Another list is:",AddList)
list.extend(AddList)
print("The Concatenated list is:",list)#Concatenating lists in python
OldElement1=input("What do you want to replace from the above list?")
NewElement=input("What do you want to replace it with?")
index1=list.index(OldElement1)
list[index1]=NewElement#Replacing list elements with new one
print("The list after the replacement with new element is:",list)
OldElement2=input("What do you want to delete from the above list?")
list.remove(OldElement2)#Deleting element from the list
print(f"List after deleting {OldElement2}:",list)
NestedList=[['Machine-learning','Generativr AI','Quantum-computing'],['Blockchain','Cryptography']]
print("The Nested list is:",NestedList)
print("~A python program by Kashish Gupta 09/231P081")




