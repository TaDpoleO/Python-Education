from collections import deque

class Tree():
    def __init__(self, size):
        if size < 1:
            self.root = None
            self.vertices = [None]
        else:
            self.root = [1, None, None, None] # val, left, right, parent
            self.vertices = [None, self.root]

            stack, curr_v = deque([self.root]), 2
            while curr_v < size+1:
                curr_node = stack.pop()
                
                next_node = [curr_v, None, None, curr_node]
                self.vertices.append(next_node)
                stack.appendleft(next_node)

                if curr_node[1] is None:
                    curr_node[1] = next_node
                    stack.append(curr_node)
                elif curr_node[2] is None:
                    curr_node[2] = next_node

                curr_v += 1

    def makeExchange(self, vertice):
        v = self.vertices[vertice]

        if v[3] is not None:
            p = v[3]

            if p[3] is not None:
                pp = p[3]

                if pp[1] is p:
                    if p[1] is v:
                        p[1] = v[1]
                        p[3] = v
                        if v[1] is not None: v[1][3] = p

                        v[1] = p
                        v[3] = pp

                        pp[1] = v
                    else:
                        p[2] = v[2]
                        p[3] = v
                        if v[2] is not None: v[2][3] = p

                        v[2] = p
                        v[3] = pp

                        pp[1] = v
                else:
                    if p[1] is v:
                        p[1] = v[1]
                        p[3] = v
                        if v[1] is not None: v[1][3] = p

                        v[1] = p
                        v[3] = pp

                        pp[2] = v
                    else:
                        p[2] = v[2]
                        p[3] = v
                        if v[2] is not None: v[2][3] = p

                        v[2] = p
                        v[3] = pp

                        pp[2] = v
            else:
                if p[1] is v:
                    p[1] = v[1]
                    p[3] = v
                    if v[1] is not None: v[1][3] = p

                    v[1] = p
                    v[3] = None
                else:
                    p[2] = v[2]
                    p[3] = v
                    if v[2] is not None: v[2][3] = p

                    v[2] = p
                    v[3] = None

                self.root = v

    def __str__(self):        
        def dfs(node, result):
            if node[1] is not None: dfs(node[1], result)
            result.append(str(node[0]))
            if node[2] is not None: dfs(node[2], result)

        result = []
        dfs(self.root, result)

        return ' '.join(result)

fin = open('input.txt')

N, Q = [int(x) for x in fin.readline().split()]
tree = Tree(N)

queries = [int(x) for x in fin.readline().split()]

for v in queries:
    tree.makeExchange(v)

print(tree)