def simple_hash(key):
    total = 0
    for ch in key:
        total += ord(ch)
    return print(total)

simple_hash('leon kennedy') # 1212
simple_hash('fox mulder') # 1014

# takes string and returns numerical sum

def multiplicative_hash(key):
    h = 1
    for ch in key:
        h = (h * 31) + ord(ch)
    return print(h)

multiplicative_hash('leon kennedy') #3617590340022339673
multiplicative_hash('fox mulder') #3614473798282495

def djb2(s):
    h = 5381
    for ch in s:
        (h << 31) + ord(ch)
    return print(h)

djb2('leon kennedy') # 5381
djb2('fox mulder') # 5381

def built_in_hash(key):
    pass

print(hash('leon kennedy')) #2456551442558548220
print(hash('fox mulder')) #-4332513793228388604

keys = ['bat', 'ball', 'tab']
for key in keys:
    hash_value = simple_hash(key)
    print(f'{key}: {hash_value} % 5') # this is a hash collision !!


# chained hashing
# key values pairs in tuple inside of each 'bucket'
# e.g. ('apples' : 5) - there can be multiple key value pairs inside each tuple

class chaining_hash_table:
    def __init__(self, size=5):
        self.size = 5
        self.table = [[] for _ in range(self.size)]

    def hashing_function(self, key):
        return sum(ord(ch) for ch in key) % self.size # hashing func % compression func

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f'{i}: {bucket}')

    def insert(self, key, value=None):
        index = self.hashing_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = ( key, value)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hashing_function(key)
        for (k, v) in self.table[index]:
            if k == key:
                return print(v)
        return None



chain_ht = chaining_hash_table()
chain_ht.insert('ball', 10)
chain_ht.insert('bat', 30)
chain_ht.insert('cat', 50)
chain_ht.insert('tab', 75)
chain_ht.insert('dog', 100)

chain_ht.display()
chain_ht.search('bat')

# linear probing

class linear_probing:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * self.size

    def hashing_function(self, key):
        return sum(ord(ch) for ch in key) % self.size

    def display(self):
        print(self.table)

    def insert(self, key):
        h = self.hashing_function(key)
        for i in range(self.size):
            index = (h + i) % self.size
            if self.table[index] is None:
                self.table[index] = key
                print(f'key: {key}, original index: {h}, new index: {index}')
                self.display()
                return True
        raise Exception('hash table is full')

    def search(self, key):
        h = self.hashing_function(key)
        for i in range(self.size):
            index = (h + i) % self.size
            if self.table[index] is None:
                return False
            if self.table[index] == key:
                return index
        return False

lp = linear_probing()
lp.insert('ball')
lp.insert('bat')
lp.insert('cat')
lp.insert('tab')
lp.insert('dog')

# quadratic probing

class quadratic_probing:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * self.size

    def hashing_function(self, key):
        return sum(ord(ch) for ch in key) % self.size

    def display(self):
        print(self.table)

    def insert(self, key):
        h = self.hashing_function(key)
        for i in range(self.size):
            index = (h + (i * i)) % self.size
            if self.table[index] is None:
                self.table[index] = key
                print(f'key: {key}, original index: {h}, new index: {index}')
                self.display()
                return True
        raise Exception('hash table is full')

    def search(self, key):
        h = self.hashing_function(key)
        for i in range(self.size):
            index = (h + (i * i)) % self.size
            if self.table[index] is None:
                return False
            if self.table[index] == key:
                return index
        return False


qp = quadratic_probing(size=9)
qp.insert('ball')
qp.insert('bat')
qp.insert('cat')
qp.insert('tab')
qp.insert('dog')

# common operations with dicts and sets
# hashing operations using dictionary 

student = {
    'name' : 'Leon S. Kennedy',
    'age' : '27',
    'gender' : 'Male'
}

 # insertion
student['nationality'] = 'American'
student.update({'age':28})
student.update({'org':'USSTRATCOM'})

student.setdefault('name') # checks if a key exists and return default
# if key doesn't exist, it returns none

student.setdefault('callsign', 'Condor One')
print(student)
student.update({'age':27, 'Objective': 'Baby Eagle'})
print(student)
print(student.popitem()) # gives last key value pair
print(student.pop('name')) # returns corresponding value and removes it



# membership - is a key present/available in the dictionary or not

print(bool('age' in student))

# iteration
for x in student:
    print(x) # by default we iterate over the keys and not the values

for k in student:
    print(f'{k}: {student[k]}')

for x in student.items():
    print(x) # returns a tuple


# hashing operations using sets

s = {'Chris', 36, 'country', 100, 22.5}

# insertion
s.add('city')
print(s)

# searching
print(bool('Chris' in s))
print(s.pop())
print(s.pop())
# randomly deletes an element

for x in s:
    print(x)


def char_count(text):
    freq = dict()
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return print(freq)

char_count('our business is life itself')

def two_sum(nums, target):
    seen = set()
    for x in nums:
        if (target - x) in seen:
            return (x, target - x)
        seen.add(x)
    return None
