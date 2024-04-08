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
            
    def find(self, val, node=None):
            if self.root is None:
                return False
            
            if node is not None:
                curr_node = node
            else:  
                curr_node = self.root

            if val == curr_node[0]:
                return True
            elif val < curr_node[0]:
                if curr_node[1] is None:
                    return False
                else:
                    return self.find(val, curr_node[1])
            elif val > curr_node[0]:
                if curr_node[2] is None:
                    return False
                else:
                    return self.find(val, curr_node[2])
   
    def format_print(self):
        def __format_print(level, node):
            if self.root is None: return None
            if node is None: node = self.root

            if node[1] is not None:  __format_print(level+1, node[1])
            print('.'*level+str(node[0]))
            if node[2] is not None:  __format_print(level+1, node[2])

        if self.root[1]: __format_print(1, self.root[1])
        print(self.root[0])        
        if self.root[2]: __format_print(1, self.root[2])

fin = open('input.txt')

tree = BinarySearchTree()
for line in fin:
    line = line.split()
    if line[0] == 'ADD':
        number = int(line[1])

        res = tree.add(number)
        if res != 0:
            print('DONE')
        else:
            print('ALREADY')
    elif line[0] == 'SEARCH':
        number = int(line[1])

        if tree.find(number):
            print('YES')
        else:
            print('NO')
    elif line[0] == 'PRINTTREE':
        tree.format_print()