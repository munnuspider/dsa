# implement queues using lists
class queue_using_list:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print('empty queue')
            return
        print(self.queue)

    def enqueue(self, data):
        self.queue.append(data)
        self.display()

    def dequeue(self):
        if self.is_empty():
            print('empty queue')
            return
        
        dequeued = self.queue.pop(0)
        self.display()
        return dequeued

    def front_peek(self):
        if self.is_empty():
            print('empty queue')
            return
        return print(self.queue[0])

    def rear_peek(self):
        if self.is_empty():
            print('empty queue')
            return
        return print(self.queue[-1])

queue_list = queue_using_list()
queue_list.is_empty()
queue_list.front_peek()
queue_list.rear_peek()
queue_list.enqueue(25)
queue_list.enqueue(45)
queue_list.enqueue(60)
queue_list.enqueue(50)
queue_list.dequeue()
queue_list.front_peek()
queue_list.rear_peek()

# implement queues using linked lists
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue_using_linked_list:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.is_empty():
            print('empty queue')
            return 
        current = self.front
        while current:
            print(current.data, end =" ")
            current = current.next
        print()

    def enqueue(self, data):
        new_node = node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.display()

    def dequeue(self):
        if self.is_empty():
            print('empty queue')
            return
        current = self.front
        self.front = current.next
        if not self.front:
            self.rear = None
        dequeued = current.data
        self.display()
        return dequeued

    def front_peek(self):
        if self.is_empty():
            print('empty queue')
            return
        return self.front.data

    def rear_peek(self):
        if self.is_empty():
            print('empty queue')
            return
        return self.rear.data

    
queue__linked_list = queue_using_list()
queue__linked_list.is_empty()
queue__linked_list.front_peek()
queue__linked_list.rear_peek()
queue__linked_list.enqueue(25)
queue__linked_list.enqueue(45)
queue__linked_list.enqueue(60)
queue__linked_list.enqueue(50)
queue__linked_list.dequeue()
queue__linked_list.front_peek()
queue__linked_list.rear_peek()

# implement queues using collections (basically a doubly linked list)
from collections import deque
class queue_using_collections:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print('empty queue')
            return
        else:
            print(self.queue)

    def enqueue(self, data):
        self.queue.append(data)
        self.display()

    def dequeue(self):
        if self.is_empty():
            print('empty queue')
            return
        dequeued = self.queue.popleft()
        self.display()
        return dequeued

    def front_peek(self):
        if self.is_empty():
            print('empty queue')
            return
        return self.queue[0]
    
    def rear_peek(self):
        if self.is_empty():
            print('empty queue')
            return
        return self.queue[-1]

class larping_queue_as_two_stacks:
    def __init__(self):
        self.stack_one = deque()
        self.stack_two = deque()

    def push(self, x: int) -> None:
        self.stack_one.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if not self.stack_two:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())
        return self.stack_two.pop()
        

    def peek(self) -> int:
        if self.empty():
            return None
        if not self.stack_two:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())
        return self.stack_two[-1]


    def empty(self) -> bool:
        return not self.stack_one and not self.stack_two



# test cases
q1 = deque()
for x in range(1, 6):
    q1.append(x)

q2 = deque()
for x in range(4, 0, -1):
    q2.append(x)

def reverse_first(queue, k):
    stack = deque()
    result = deque()

    for _ in range(k):
        stack.append(queue.popleft())

    while stack:
        result.append(stack.pop())

    while queue:
        result.append(queue.popleft())
    return print(result)

reverse_first(q1, 3)
reverse_first(q2, 4)

def ticket_counter(n, k):
    queue = deque()
    if n == 1:
        return n

    for x in range(1, n + 1):
        queue.append(x)

    while True:
        for _ in range(k):
            queue.popleft()
            if len(queue) == 1:
                return print(queue[0])

        for _ in range(k):
            queue.pop()
            if len(queue) == 1:
                return print(queue[0])

        
ticket_counter(9, 3)


