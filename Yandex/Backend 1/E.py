import sys
sys.setrecursionlimit(1000000)

fin = open('input.txt')

N = int(fin.readline())

ingredients = [[] for _ in range(N+1)]

for i in range(3, N+1):
    _, *ingredient = [int(x) for x in fin.readline().split()]
    ingredients[i] = ingredient

potions = [(0, 0) for _ in range(N+1)]

def ingredientsToAB(S):
    if S in visited: return (float('inf'), float('inf'))   
    visited.add(S)

    A = B = 0

    for ing in ingredients[S]:
        if ing == 1:
            A += 1
        elif ing == 2:
            B += 1
        else:          
            if potions[ing] != (0, 0):                
                A += potions[ing][0]
                B += potions[ing][1]
            else:
                potions[ing] = ingredientsToAB(ing)
                A += potions[ing][0]
                B += potions[ing][1]

                if A > 10**9 or B > 10**9:
                    A = float('inf')
                    B = float('inf')
                    break

    visited.remove(S)
    return A, B

for i in range(3, N+1):
    visited = set()
    if potions[i] == (0, 0): potions[i] = ingredientsToAB(i)

Q = int(fin.readline())
answer = [0]*Q

def isEnoughIngredients(X, Y, S):
    if X >= potions[S][0] and Y >= potions[S][1]:
        return True
    else:
        return False

for i in range(Q):
    X, Y, S = [int(x) for x in fin.readline().split()]

    if isEnoughIngredients(X, Y, S):
        answer[i] = '1'
    else:
        answer[i] = '0'

print(''.join(answer))