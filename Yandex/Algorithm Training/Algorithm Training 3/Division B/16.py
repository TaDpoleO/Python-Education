class Stack():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def push(self, val):
        if self.head is None:
            self.head = [val, None, None]
            self.tail = self.head
        else:
            self.tail[1] = [val, None, None]
            self.tail[1][2], self.tail = self.tail, self.tail[1]
        self.length += 1

        return 'ok'
    
    def pushleft(self, val):
        if self.head is None:
            self.head = [val, None, None]
            self.tail = self.head
        else:
            self.head[2] = [val, None, None]
            self.head[2][1], self.head = self.head, self.head[2]
        self.length += 1

        return 'ok'    
        
    def pop(self):
        if self.tail is None: return 'error'
        res = self.tail[0]

        if self.tail[2] is not None:
            self.tail[2][1], self.tail[2], self.tail = None, None, self.tail[2]
            self.length -= 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

        return res
    
    def popleft(self):
        if self.head is None: return 'error'
        res = self.head[0]

        if self.head[1] is not None:
            self.head[1][2], self.head[1], self.head = None, None, self.head[1]
            self.length -= 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

        return res    
            
    def back(self):
        if self.tail is None: return 'error'
        return self.tail[0]
    
    def front(self):
        if self.head is None: return 'error'
        return self.head[0]    
            
    def size(self):
        return self.length
        
    def clear(self):
        self.__init__()
        return 'ok'
    
    def __str__(self):
        return str(self.head)
        
stack = Stack()
fin = open('input.txt')

while True:
    command, *args = fin.readline().split()
    if command == 'exit':
        print('bye')
        break
    elif command == 'push':
        print(stack.push(args[0]))
    elif command == 'pop':
        print(stack.popleft())
    elif command == 'front':
        print(stack.front())
    elif command == 'size':
        print(stack.size())
    elif command == 'clear':
        print(stack.clear())