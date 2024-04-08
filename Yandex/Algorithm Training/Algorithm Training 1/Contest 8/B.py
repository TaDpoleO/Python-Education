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
        
fin = open('input.txt')
numbers = [int(x) for x in fin.readline().split()]
numbers.pop()

tree = BinarySearchTree()
for num in numbers:
    level = tree.add(num)
    if level != 0: print(level, end=' ')