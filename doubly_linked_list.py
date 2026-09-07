class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list():
    def __init__(self):
        self.head = None
        self.tail = None # for our convenience
        self.length = 0

    def is_empty(self):
        return self.head is None

    def display_forward(self):
        if self.is_empty():
            print('empty list')
        else:
            current = self.head
            while current:
                print(current.data, end=' <--> ' if current.next else '\n')
                current = current.next

    def display_backward(self):
        if self.is_empty():
            print('empty list')
        else:
            current = self.tail
            while current:
                print(current.data, end=' <--> ' if current.prev else '\n')
                current = current.prev

    def insert_at_beginning(self, value):
        new_node = node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        self.display_forward()

    def insert_at_end(self, value):
        new_node = node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        self.display_forward()

    def insertion(self, position, value):
        n = self.length
        if (position < 0) or (position > n):
            print('invalid index')
            return

        if position == 0:
            self.insert_at_beginning(value)
        elif position == n:
            self.insert_at_end(value)
        else:
            new_node = node(value)
            l = self.head
            for _ in range(position):
                l = l.next
            m = l.prev
            m.next = new_node
            new_node.prev = m
            new_node.next = l
            l.prev = new_node
            self.length += 1
            self.display_forward()

    def search(self, key):
        if self.is_empty():
            print('empty list')
            return
        
        position = 0
        current = self.head
        while current:
            if current.data == key:
                print(f"{key} found at index {position}")
                return
            position += 1
            current = current.next
        print(f"{key} not found in list")

    def delete_at_beginning(self):
        if self.is_empty():
            print('empty list')
            return

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current = self.head
            self.head = self.head.next
            self.head.prev = None
            current.next = None
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
            current = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            current.prev = None
        self.length -= 1
        self.display_forward()

    def deletion(self, position):
        if self.is_empty():
            print('empty list')
            return
        n = self.length
        if (0 > position) or (position >= n):
            print('invalid index')
        elif position == 0:
            self.delete_at_beginning()
        elif position == n- 1:
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
            self.display_forward()

        
          

dll = doubly_linked_list()
dll.display_backward()
dll.display_forward()
dll.insert_at_beginning(30)
dll.insert_at_beginning(40)
dll.insert_at_beginning(50)
dll.insert_at_beginning(60)
dll.insert_at_beginning(70)
dll.insert_at_end(80)
dll.insert_at_end(90)
dll.display_backward()
dll.display_forward()
dll.insertion(3, 55)
dll.insertion(8, 55)
dll.search(60)
dll.delete_at_beginning()
dll.delete_at_end()
dll.deletion(3)