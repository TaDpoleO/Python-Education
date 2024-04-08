from collections import deque

fin = open('input.txt')
deck1 = deque([int(x) for x in fin.readline().split()])
deck2 = deque([int(x) for x in fin.readline().split()])

def answer(deck1, deck2):
    moves = 0
    
    while deck1 and deck2:
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        
        if (card1 == 0 and card2 == 9):
            deck1.append(card1)
            deck1.append(card2)
        elif (card1 == 9 and card2 == 0):
            deck2.append(card1)
            deck2.append(card2)
        elif (card1 > card2):
            deck1.append(card1)
            deck1.append(card2)            
        elif (card1 < card2):
            deck2.append(card1)
            deck2.append(card2)               
            
        moves += 1
        if moves == 10**6: return 'botva'
        
    if deck1:
        return f'first {moves}'
    else:
        return f'second {moves}'
    
print(answer(deck1, deck2))