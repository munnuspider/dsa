#implementing stacks using a list

class my_stack:
    def __init__(self):
        self.stack = [] # defining the stack as a list

    def get_size(self):
        return len(self.stack)

    def is_empty(self):
        return self.get_size() == 0

    def display(self):
        if self.is_empty():
            print('empty stack')
            return 
        for element in self.stack[::-1]:
            print(element)
        print()

    def push(self, data):
        self.stack.append(data)
        self.display()
        print(f'pushed element {data}')

    def pop(self):
        if self.is_empty():
            print('empty stack')
            return None
        popped = self.stack.pop()
        self.display()
        print(f'popped element {popped}')

    def peek(self):
        if self.is_empty():
            print('empty stack')
            return None

        print(f'peek element: {self.stack[-1]}')

s = my_stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.push(70)
s.pop()
s.peek()
s.display()

#implement a stack using the collections module

from collections import deque

stack = deque()
stack.append(15)
stack.append(35)
stack.append(50)
stack.append(10)
stack.pop()
print(stack, len(stack)) # display
print(stack[-1]) # peek


#implementing a stack using a singly linked list

class node():
    def __init__(self, data):
        self.data = data
        self.next = None

class stack_linked_list:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.is_empty():
            print('empty stack')
            return
        current = self.top
        while current:
            print(current.data)
            current = current.next
        print()

    def push(self, data):
        new_node = node(data)
        new_node.next = self.top
        self.top = new_node
        print(f'pushed element: {data}')
        self.display()

    def pop(self):
        if self.is_empty():
            print('empty stack')
            return None
        popped = self.top.data
        self.top = self.top.next
        print(f'popped element: {popped}')
        self.display()

    def peek(self):
        if self.is_empty():
            print('empty stack')
            return None
        print(f'peek element: {self.top.data}')


stacker = stack_linked_list()

stacker.push(10)
stacker.push(20)
stacker.push(30)
stacker.push(40)
stacker.push(50)
stacker.pop()
stacker.peek()

def reverse_using_stack(s):
    stack = deque()
    result = ""
    for ch in s:
        stack.append(ch)

    while stack:
        result += stack.pop()

    return print(result)

reverse_using_stack("leon")

def check_balanced_parenthesis(s):
    stack = deque()
    pairs = {
        ')':'(',
        ']':'[',
        '}':'{',
    }

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            pair = pairs[ch]
            popped = stack.pop()
            if (not stack) or pair != popped:
                return False
    return len(stack) == 0

def simulate_undo_operation(commands):
    stack = deque()

    for command in commands:
        if command == 'undo':
            if stack:
                stack.pop()
            else:
                print('empty stack')
                return
        else:
            stack.append(command[-1])
    return ''.join(stack)

commands = [
    'type A',
    'type B',
    'undo',
    'type C',
    'undo',
    'undo',
    'type L',
    'type E',
    'type O',
    'type N',
]

res = simulate_undo_operation(commands)
print(f'result: {res}')

# the most recently typed letter must be removed first

