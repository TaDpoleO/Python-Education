from collections import deque

class BinarySearchTree():
    def __init__(self, val=None, left=None, right=None) -> None:
        if val is not None:
            self.root = [val, left, right]
        else:
            self.root = None

    def add(self, val, node=None, level=1):
        if self.root is None:
            self.root = [val, None, None]
            return 1
        
        if node is not None:
            curr_node = node
        else:  
            curr_node = self.root
            level = 1

        if val == curr_node[0]:
            return 0
        elif val < curr_node[0]:
            if curr_node[1] is None:
                curr_node[1] = [val, None, None]
                return level+1
            else:
                return self.add(val, curr_node[1], level+1)
        elif val > curr_node[0]:
            if curr_node[2] is None:
                curr_node[2] = [val, None, None]
                return level+1
            else:
                return self.add(val, curr_node[2], level+1)
                
    def getLength(self, node=None):
        if self.root is None: return 0
        if node is None: return 0

        stack = deque([(node, 1)])
        while stack:
            curr_node, curr_level = stack.pop()

            if curr_node[1] is not None: stack.appendleft((curr_node[1], curr_level+1))
            if curr_node[2] is not None: stack.appendleft((curr_node[2], curr_level+1))

        return curr_level
    
    def getMaxVal(self, node=None):
        if self.root is None: return None
        if node is None: node = self.root

        curr_node, prev_node = node, None
        while curr_node is not None:
            curr_node, prev_node = curr_node[2], curr_node

        if prev_node is None:
            return None
        else:
            return prev_node[0]
    
    def getPreMaxVal(self, node=None):
        if self.root is None: return None
        if node is None: node = self.root

        curr_node, prev_node, prev_prev_node = node, None, None
        while curr_node is not None:
            curr_node, prev_node, prev_prev_node = curr_node[2], curr_node, prev_node

        if prev_node is None:
            return None
        else:
            if prev_node[1] is not None:
                return self.getMaxVal(prev_node[1])
            else:
                if prev_prev_node is not None:
                    return prev_prev_node[0]
                else:
                    return None
                
    def inorder(self, action, node=None):
        if self.root is None: return None
        if node is None: node = self.root

        if node[1] is not None:  self.inorder(action, node[1])
        action(node)
        if node[2] is not None:  self.inorder(action, node[2])        

    def __len__(self):
        return self.getLength(self.root)
    
    def __str__(self):
        return str(self.root)
        
fin = open('input.txt')
numbers = [int(x) for x in fin.readline().split()]
numbers.pop()

def print_node(node):
    if node[1] is None and node[2] is None:
        print(node[0])

tree = BinarySearchTree()
for num in numbers:
    tree.add(num)

tree.inorder(print_node)