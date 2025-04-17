#NAME: KASHISH GUPTA 231P081/09 SECOMPS A
"""Write a Menu driven program for data strutures Stack."""
# Python code to demonstrate Implementing stack using list 
stack=[]
def push():
    item = input("Enter item to push: ")
    stack.append(item)
    print(f"Item '{item}' pushed to stack")
def pop():
    if len(stack) == 0:
        print("Stack is empty! Cannot pop.")
    else:
        popped_item = stack.pop()
        print(f"Item '{popped_item}' popped from stack")
def display():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("Current stack:", stack)
def main():
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            push()
        elif choice == '2':
            pop()
        elif choice == '3':
            display()
        elif choice == '4':
            print("Exiting the program.")
            print("~A program written by kashish gupta 231P081/09 SECOMPS A")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
