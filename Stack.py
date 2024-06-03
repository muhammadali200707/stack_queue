class Stack:
    def __init__(self):
        self.data = []  # This creates list

    def is_empty(self):
        return len(self.data) == 0  # This checks list is empty or no !

    def push(self, datum):
        self.data.append(datum)  # This appends new data to the list , to the end !

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            print("Stack is empty")  # This checks if the list is non-starting and if the list is not empty,
            # it deletes from end of list if list empty it return message !

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        return "Stack is empty"  # This  show last element without deleting !

    def size(self):
        return len(self.data)  # This shows length of data !


# Here 5 examples for push ------ --------------------------------------------------------->
stack = Stack()
stack.push("Ali")
stack.push("Bob")
stack.push(90)
stack.push('Hasan')
stack.push(777)

# print(stack.data)  # This will print data


# Here 5 examples for pop ----------------------------------------------------------------->
"""print(f"This is before pop -> {stack.data}")
print(f"Deleted information -> {stack.pop()}")
print(f"This is after pop -> {stack.data}")  # Here "777" deleted

print(f"This is before pop -> {stack.data}")
print(f"Deleted information -> {stack.pop()}")
print(f"This is after pop -> {stack.data}")  # Here "Hasan" deleted

print(f"This is before pop -> {stack.data}")
print(f"Deleted information -> {stack.pop()}")
print(f"This is after pop -> {stack.data}")  # Here "90" deleted

print(f"This is before pop -> {stack.data}")
print(f"Deleted information -> {stack.pop()}")
print(f"This is after pop -> {stack.data}")  # Here "Bob" deleted

print(f"This is before pop -> {stack.data}")
print(f"Deleted information -> {stack.pop()}")
print(f"This is after pop -> {stack.data}")  # Here "Ali" deleted"""

# Here 5 examples for peek ---------------------------------------------------------------->
"""print(f"This is  peek -> {stack.peek()}")  # It will print "777"
stack.pop()  # Its just remove last element

print(f"This is  peek -> {stack.peek()}")  # It will print "Hasan"
stack.pop()  # Its just remove last element

print(f"This is  peek -> {stack.peek()}")  # It will print "90"
stack.pop()  # Its just remove last element

print(f"This is  peek -> {stack.peek()}")  # It will print "Bob"
stack.pop()  # Its just remove last element

print(f"This is  peek -> {stack.peek()}")  # It will print "Ali"
stack.pop()  # Its just remove last element"""

# Here 5 examples for size ---------------------------------------------------------------->
"""print(f"This is size of data -> {stack.size()}") 

print(f"This is size of data -> {stack.size()}")
stack.push("Kia")
print(f"This is size after adding data -> {stack.size()}") 

print(f"This is size of data -> {stack.size()}")
stack.pop()  # Its just remove last element
print(f"This is size after deleting data -> {stack.size()}")

print(f"This is size of data -> {stack.size()}")
stack.peek()
print(f"This is size after peek data -> {stack.size()}")

print(f"This is size of data -> {stack.size()}")
stack.push("989898")
print(f"This is size after adding data -> {stack.size()}")"""













































class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)


# Example usage:
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(123)

# print("Queue:", queue.items)
# front_item = queue.dequeue()
# print("Dequeued:", front_item)
# print("Queue after dequeue:", queue.items)
#
# peeked_item = queue.peek()
# print("Peeked:", peeked_item)
# print("Queue size:", queue.size())




