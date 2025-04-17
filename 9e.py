# NAME: KASHISH GUPTA 231P081/09 SECOMPS A
"""Write a program to implement circular queue."""

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!")
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            i = self.front
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.size
            print(self.queue[self.rear])

# Main Program
size = int(input("Enter the size of the queue: "))
cq = CircularQueue(size)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        value = int(input("Enter value to enqueue: "))
        cq.enqueue(value)
    elif choice == 2:
        cq.dequeue()
    elif choice == 3:
        cq.display()
    elif choice == 4:
        print("Exiting program... ThankYou KASHISH GUPTA 09 231P081")
        break
    else:
        print("Invalid choice! Please try again.")
