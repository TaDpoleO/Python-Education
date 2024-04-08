from collections import defaultdict

fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]

graph = defaultdict(set)
for line in fin:
    x, y = [int(x) for x in line.split()]
    graph[x].add(y)
    graph[y].add(x)
  
def answer(graph):
    visited, colors = set(), dict()
    
    for student in graph:          
        if student not in visited:
            visited.add(student)
            colors[student] = 0
            
            stack = [(student)]
            while stack:
                curr_student = stack.pop()

                for next_student in graph[curr_student]:
                    if next_student not in colors:
                        colors[next_student] = (colors[curr_student]+1)%2
                    else:
                        if colors[next_student] != (colors[curr_student]+1)%2: return False

                    if next_student not in visited:
                        visited.add(next_student)
                        stack.append((next_student))
                        
    return True

print('YES') if answer(graph) else  print('NO')