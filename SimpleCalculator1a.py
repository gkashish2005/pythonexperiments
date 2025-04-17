"""AIM: Write a program to perform menu driven arithmetic operation.
   NAME:KASHISH GUPTA 09/231P081"""
while True:
    print("MENU DRIVEN ARITHMETIC OPERATION")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Power")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    if choice >=1 and choice<=6:
        print("Enter the first number")
        num1=float(input())
        print("Enter the second number")
        num2=float(input())
        if choice==1:
            result=num1+num2
            print("Addition is",result)
        elif choice==2:
            result=num1-num2
            print("Subtraction is",result)
        elif choice==3:
            result=num1*num2
            print("Multiplication is",result)
        elif choice==4:
            result=num1/num2
            print("Division is",result)
        elif choice==5:
            result=num1**num2
            print("Power is",result)
        elif choice==6:
            print("Exitting.....")
            break
    else:
        print("Invalid Choice")
print("~A python program by Kashish Gupta 09/231P081")         
            
            
        
