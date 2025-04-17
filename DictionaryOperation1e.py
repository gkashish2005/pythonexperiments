"""WAP to implement following
1.Create Dictionary(key-value)
2.Iterate values from a Dictionary
3.Update value of any  key
4.Add a new Key-value pair in a dictionary
5.Delete key value pair from a dictionary
6.Set Default value and display
Name:Kashish Gupta 09/231P081"""
Dictionary={"Name":"Kashish","uin":"231P081","class":"SE-COMPS","roll-no":"09","div":"A"}#Create a dictionary
print("The dictionary is:",Dictionary)
n=1
for i in Dictionary.values():#Iterate values from a Dictionary
    print(f"Iteration {n} :",i)
    n=n+1
UpdateKey=input("Enter the key whose value is to be updated:")#Update value of any  key
UpdateValue=input(f"Enter the new value to update {UpdateKey}:")
Dictionary[UpdateKey]=UpdateValue
print(f"The Dictionary after updating the value of the {UpdateKey} is:",Dictionary)
Dictionary["Father-Name"]="Subhash Gupta"#Add a new Key-value pair in a dictionary
print("The dictionary after adding a new key-value pair:",Dictionary)
Delete=input("Enter the key you want to delete from the dictionary:")#Delete key value pair from a dictionary
del Dictionary[Delete]
print(f"Dictionary aafter the deletion of the {Delete} is:",Dictionary)
Dictionary.setdefault("city","Nallasopara")#Set Default value and display
print("The dictionary after setting default value: ", Dictionary)
print("~A program by Kashish Gupta 09/231P081")
