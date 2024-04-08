import sys

fin = sys.stdin
# fin = open('input.txt')

N = int(fin.readline())
books = set([int(x) for x in fin.readline().split()])

def answer(books):
    if len(books) == 1: return str(books[0])

    books = sorted(books)
    stack = [(books[0], books[0])]
    for book in books[1:]:
        if book == stack[-1][1]+1:
            last = stack.pop()
            stack.append((last[0], book))
        else:
            stack.append((book, book))

    res = []
    for segment in stack:
        if segment[0] == segment[1]:
            res.append(str(segment[0]))
        elif segment[0] == segment[1]-1:
            res.append(str(segment[0]))
            res.append(str(segment[1]))
        else:
            res.append(str(segment[0]))
            res.append('...')
            res.append(str(segment[1]))            
    
    return ' '.join(res)

print(answer(books))