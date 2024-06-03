class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return "Queue is empty"
        else:
            return "Queue is not empty"

    def enqueue(self, datum):
        self.data.append(datum)

    def dequeue(self):
        if self.is_empty():
            return self.data.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if self.is_empty():
            return self.data[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.data)


# Here 5 examples for enqueue --------------------------------------------------------------------->
"""queue = Queue()
queue.enqueue("John")
queue.enqueue(123)
queue.enqueue("Dad")
queue.enqueue(343)
queue.enqueue(456)"""

# Here 5 examples for dequeue --------------------------------------------------------------------->
"""print(f"This is before dequeue {queue.data}")
print(f"Deleted element -> {queue.dequeue()}")
print(f"This is after dequeue {queue.data}")  # This delete John

print(f"This is before dequeue {queue.data}")
print(f"Deleted element -> {queue.dequeue()}")
print(f"This is after dequeue {queue.data}")  # This delete 123

print(f"This is before dequeue {queue.data}")
print(f"Deleted element -> {queue.dequeue()}")
print(f"This is after dequeue {queue.data}")  # This delete Dad

print(f"This is before dequeue {queue.data}")
print(f"Deleted element -> {queue.dequeue()}")
print(f"This is after dequeue {queue.data}")  # This delete 343

print(f"This is before dequeue {queue.data}")
print(f"Deleted element -> {queue.dequeue()}")
print(f"This is after dequeue {queue.data}")  # This delete 456"""

# Here 5 examples for peek ----------------------------------------------------------------------->
"""print(f"This is  peek -> {queue.peek()}")  # It will print "John"
queue.dequeue()  # Its just remove last element

print(f"This is  peek -> {queue.peek()}")  # It will print "123"
queue.dequeue()  # Its just remove last element

print(f"This is  peek -> {queue.peek()}")  # It will print "Dad"
queue.dequeue()  # Its just remove last element

print(f"This is  peek -> {queue.peek()}")  # It will print "343"
queue.dequeue()  # Its just remove last element

print(f"This is  peek -> {queue.peek()}")  # It will print "456"
queue.dequeue()  # Its just remove last element"""

# Here 5 examples for size ----------------------------------------------------------------------->
"""print(f"This is size of data -> {queue.size()}")

print(f"This is size of data -> {queue.size()}")
queue.enqueue("Lambo")
print(f"This is size after adding data -> {queue.size()}")

print(f"This is size of data -> {queue.size()}")
queue.dequeue()  # Its just remove last element
print(f"This is size after deleting data -> {queue.size()}")

print(f"This is size of data -> {queue.size()}")
queue.peek()
print(f"This is size after peek data -> {queue.size()}")

print(f"This is size of data -> {queue.size()}")
queue.enqueue("989898")
print(f"This is size after adding data -> {queue.size()}")"""


