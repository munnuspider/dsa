class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class circular_doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def display_forward(self):
        if self.is_empty():
            print('empty list')
            return
        else: 
            current = self.head
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break
            print()
        
    def display_backward(self):
        if self.is_empty():
            print('empty list')
            return
        else:
            current = self.tail
            while True:
                print(current.data, end=" ")
                current = current.prev
                if current == self.tail:
                    break
            print()

    def insert_at_beginning(self, data):
        new_node = node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            # self.head = self.tail = new_node
            # new_node.next = new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.length += 1
        self.display_forward()

    def insert_at_end(self, data):
        new_node = node(data)
        if self.is_empty():
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        self.display_forward()

    def insertion(self, position, data):
        n = self.length
        if (0 > position) or (n < position):
            print('invalid index')
            return
        if position == 0:
            self.insert_at_beginning(data)
        elif position == n:
            self.insert_at_end(data)
        else:
            new_node = node(data)
            l = self.head
            m = None
            for _ in range(position):
                l = l.next
            m = l.prev
            m.next = new_node
            new_node.prev = m
            new_node.next = l
            l.prev = new_node
            self.display_forward()
        self.length += 1

    def search(self, key):
        if self.is_empty():
            print('empty list')
            return
        else:
            current = self.head
            position = 0
            while True:
                current = current.next
                position += 1
                if current.data == key:
                    print(f'{key} found at index {position}')
                    break
                if current == self.head:
                    print(f'{key} not found')
                    break

    def delete_at_beginning(self):
        if self.is_empty():
            print('empty list')
            return

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        self.display_forward()

    def delete_at_end(self):
        if self.is_empty():
            print('empty list')
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        self.display_forward()

    def deletion(self, position):
        n = self.length
        if self.is_empty():
            print('empty list')
            return
        if (position < 0) or (position >= n):
            print('invalid index')
            return
        elif position == 0:
            self.delete_at_beginning()
        elif position == n - 1:
            self.delete_at_end()
        else:
            l = self.head
            m = None
            for _ in range(position):
                l = l.next
            m = l.prev
            m.next = l.next
            l.next.prev = m
            l.next = None
            l.prev = None
        self.length -= 1
        self.display_forward() 


    
cdll = circular_doubly_linked_list()
cdll.display_forward()
cdll.display_backward()
cdll.insert_at_beginning(10)
cdll.insert_at_end(20)
cdll.insert_at_beginning(5)
cdll.insert_at_end(30)
cdll.insertion(2, 15)
cdll.insertion(0, 3)
cdll.search(10)
cdll.search(30)
cdll.search(359)
cdll.delete_at_beginning()
cdll.delete_at_end()
cdll.deletion(2)
