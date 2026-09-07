class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singly_linked_list:
    def __init__(self):
        self.head = None

    def get_length(self):
        length = 0
        current = self.head
        while current: # falsy in python
            length += 1
            current = current.next
        return length

    def display(self):
        if not self.head:
            print("empty list")
        else:
            current = self.head
            while current:
                print(current.data, end=' ')
                current = current.next
            print()

    def insertion_at_beginning(self, value):
        new_node = node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.display()

    def insertion_at_end(self, value):
        new_node = node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        self.display()

    def insertion(self, position, value):
        n = self.get_length()
        if (0 > position) or (position > n):
            print('invalid index')
        elif position == 0:
            self.insertion_at_beginning(value)
        elif position == n:
            self.insertion_at_end(value)
        else:
            new_node = node(value)
            l = self.head
            m = None
            for _ in range(position):
                m = l
                l = l.next
            m.next = new_node
            new_node.next = l
            self.display()       

    def search(self, key):
        if not self.head:
            print('list is empty')
        else:
            position = 0
            current = self.head
            while current:
                if current.data == key:
                    print(f"{key} found at position {position}")
                    return
                position += 1
                current = current.next
            print(f"{key} not found in list" )

    def delete_at_beginning(self):
        if self.head:
            current = self.head
            self.head = current.next
            current.next = None
        else:
            print('cannot delete from an empty list')

    def delete_at_end(self):
        if self.head:
            l = self.head
            q = None
            while l.next:
                m = l
                l = l.next
                if l == self.head:
                    self.head = None
                else:
                    m.next = None
        else:
            print('cannot delete from an empty list')

    def deletion(self, position):
        n = self.get_length()
        if (position < 0) or (position >= n):
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
        self.display()

    def find_middle(self):
        n = self.get_length()
        traverse = n // 2
        current = self.head
        for _ in range(traverse):
            current = current.next
        return print(current.data)

    def find_sum(self):
        current = self.head
        sum = 0
        if not self.head:
            return 0
        
        while current:
            sum += current.data
            current = current.next
        return print(f'sum of nodes is {sum}')

    def find_max(self):
        if not self.head:
            return None
        max_num = 0
        current = self.head
        while current:
            if max_num < current.data:
                max_num = current.data
            current = current.next
        return print(f'maximum number is {max_num}')

    def find_min(self):
        if not self.head:
            return None
        current = self.head
        min_num = current.data
        while current:
            if min_num > current.data:
                min_num = current.data
            current = current.next
        return print(f'minimum number is {min_num}')

    


            

sll = singly_linked_list()
sll.insertion_at_end(30)
sll.insertion_at_end(40)
sll.insertion_at_end(50)
sll.insertion_at_end(60)
sll.insertion_at_end(70)
sll.insertion_at_end(75)
sll.insertion_at_end(80)
sll.insertion_at_end(90)
sll.deletion(0)
sll.find_middle()
sll.find_sum()
sll.find_max()
sll.find_min()