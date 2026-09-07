class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circular_singly_linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def display(self):
        if self.is_empty():
            print('empty list')
        else:
            current = self.head
            while True:
                print(current.data, end=' ')
                current = current.next
                if current == self.head:
                    break
            print()

    def insert_at_beginning(self, value): # the difference here is that the new node that is added becomes the new head of the csll
        new_node = node(value)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        self.display()

    def insert_at_end(self, value):
        new_node = node(value)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.length += 1
        self.display()

    def insertion(self, position, value):
        n = self.length
        if (0 > position) or (n < position): 
            print('invalid index')
        elif position == 0:
            self.insert_at_beginning(value)
        elif position == n:
            self.insert_at_end(value)
        else:
            new_node = node(value)
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1
            self.display()

    def search(self, key):
        if self.is_empty():
            print('empty list')
            return 
        
        position = 0
        current = self.head
        while True:
            if current.data == key:
                print(f"{key} found at index {position}")
                return
            position += 1
            current = current.next
            if current == self.head:
                break
        print(f"{key} not found in list")

    def delete_at_beginning(self):
        if self.is_empty():
            print('cannot delete from an empty list')
            return
        if self.length == 1:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            self.head = self.head.next
            current.next = self.head
        self.length -= 1
        self.display()

    def delete_at_end(self):
        if self.is_empty():
            print('cannot delete from empty list')
            return
        if self.length == 1:
            self.head = None
        else:
            l = self.head
            m = None
            while l.next != self.head:
                m = l
                l = l.next
            m.next = self.head
            l.next = None 
        self.length -= 1
        self.display()

    def deletion(self, position):
        if self.is_empty():
            print('cannot delete from empty list')
            return
        
        n = self.length
        if (0 > position) or (position > n):
            print('invalid index')
        elif position == 0:
            self.delete_at_beginning()
        elif position == n - 1:
            self.delete_at_end()
        else:
            l = self.head
            m = None
            for _ in range(position):
                m = l
                l = l.next
            m.next = l.next
            l.next = None
        self.length -= 1
        self.display()

    def count_nodes(self):
        if self.is_empty():
            return 0
        else:
            current = self.head
            count = 1
            while current.next != self.head:
                current = current.next
                count += 1
            return print(f'number of nodes: {count}')

        


csll = circular_singly_linked_list()
csll.display()
csll.is_empty()
csll.insert_at_beginning(10)
csll.insert_at_beginning(20)
csll.insert_at_beginning(30)
csll.insert_at_beginning(40)
csll.insert_at_beginning(50)
csll.insert_at_end(60)
csll.insertion(3, 35)
csll.insertion(0, 55)
csll.insertion(8, 65)
csll.search(30)
csll.search(45)
csll.delete_at_beginning()
my_csll = circular_singly_linked_list()
my_csll.insert_at_end(10)
my_csll.delete_at_end()
csll.delete_at_end()
csll.deletion(4)
csll.count_nodes()
