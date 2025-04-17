# NAME: KASHISH GUPTA 231P081/09
"""Write a program for cutting tickets and show chair thread."""
from threading import Thread, Lock
from time import sleep
class Theatre:
    # Constructor
    def __init__(self, str, lock):
        self.str = str
        self.lock = lock

    # Method repeat for 5 tickets
    def movieshow(self):
        for i in range(1, 6):
            with self.lock:  # Acquire the lock to ensure thread-safe printing
                print(self.str, ":", i)
                sleep(0.5)
# Create a lock for synchronizing the threads
lock = Lock()
# Create two instances of the Theatre class
obj1 = Theatre("Cut Ticket", lock)
obj2 = Theatre("Show Chair", lock)
# Create two threads to run movieshow()
t1 = Thread(target=obj1.movieshow)
t2 = Thread(target=obj2.movieshow)
# Start the threads
t1.start()
t2.start()
# Wait for both threads to finish
t1.join()
t2.join()
print("\nThankYou KASHISH GUPTA 09 231P081")
