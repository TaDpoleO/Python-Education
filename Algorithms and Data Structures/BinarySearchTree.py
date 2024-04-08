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
            
    def delete(self, val, node=None, prev_node=None):
        if self.root is None: return False

        if node is not None:
            curr_node = node
        else:  
            curr_node = self.root              
            
        if val == curr_node[0]:
            if curr_node[1] is not None and curr_node[2] is not None:
                prev_left_max_node, left_max_node = curr_node, curr_node[1]
                while left_max_node[2] is not None:
                    prev_left_max_node = left_max_node
                    left_max_node = left_max_node[2]
                temp_val = left_max_node[0]
                self.delete(left_max_node[0], left_max_node, prev_left_max_node)
                curr_node[0] = temp_val
            elif curr_node[1] is not None:
                curr_node[0], curr_node[1], curr_node[2] = curr_node[1][0], curr_node[1][1], curr_node[1][2]
            elif curr_node[2] is not None:
                curr_node[0], curr_node[1], curr_node[2] = curr_node[2][0], curr_node[2][1], curr_node[2][2]
            else:
                if prev_node is None:
                    self.root = None
                else:
                    if curr_node[0] > prev_node[0]:
                        prev_node[2] = None
                    else:
                        prev_node[1] = None                        
            return True
        elif val < curr_node[0]:
            if curr_node[1] is None:
                return False
            else:
                return self.delete(val, curr_node[1], curr_node)
        elif val > curr_node[0]:
            if curr_node[2] is None:
                return False
            else:
                return self.delete(val, curr_node[2], curr_node)
                           
    def getHeight(self, node=None):
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

    def preorder(self, action, node=None):
        if self.root is None: return None
        if node is None: node = self.root

        action(node)
        if node[1] is not None:  self.preorder(action, node[1])        
        if node[2] is not None:  self.preorder(action, node[2])

    def postorder(self, action, node=None):
        if self.root is None: return None
        if node is None: node = self.root
        
        if node[1] is not None:  self.postorder(action, node[1])        
        if node[2] is not None:  self.postorder(action, node[2])
        action(node)

    def isAVLTree(self, node=None):
        if self.root is None: return False
        if node is None: node = self.root

        if abs(self.getHeight(node[1])-self.getHeight(node[2]))<=1:
            if (node[1] is not None) and (node[2] is not None):
                return self.isAVLTree(node[1]) and self.isAVLTree(node[2])
            elif (node[1] is not None):
                return self.isAVLTree(node[1])
            elif (node[2] is not None):
                return self.isAVLTree(node[2])
            else:
                return True
        else:
            return False

    def __len__(self):
        return self.getHeight(self.root)
    
    def __str__(self):
        return str(self.root)

if __name__ == '__main__':
    numbers = [7, 6, 4, 5, 8, 9, 20, 1, 2, 3]

    tree = BinarySearchTree()
    for num in numbers:
        tree.add(num)
    print(tree)

    print('-'*50)
    print('Deleting\n')
    numbers = [4, 8, 20, 100]
    print(numbers)
    for num in numbers:
        print(tree.delete(num))
    print(tree)

    print('-'*50)
    print('Search\n')
    numbers = [7, 4, 100, 8, 6, 5, 9, 1, 20]
    print(numbers)
    for num in numbers:
        print(tree.find(num))