inp_file = open('input.txt')

def answer():  
    FLAG_CONSTANT = True
    FLAG_ASCENDING = True
    FLAG_WEAKLY_ASCENDING = True
    FLAG_DESCENDING = True
    FLAG_WEAKLY_DESCENDING = True
    
    prev = int(inp_file.readline())
    while True:
        curr = int(inp_file.readline())
        if curr == -2000000000: break
        
        
        if curr != prev:
            FLAG_CONSTANT = False
        
        if curr == prev:
           FLAG_ASCENDING = False
           FLAG_DESCENDING = False
           
        if curr < prev:
            FLAG_ASCENDING = False
            FLAG_WEAKLY_ASCENDING = False
            
        if curr > prev:
            FLAG_DESCENDING = False
            FLAG_WEAKLY_DESCENDING = False
            
        prev = curr
        
    if FLAG_CONSTANT:
        return 'CONSTANT'
    elif FLAG_ASCENDING:
        return 'ASCENDING'
    elif FLAG_WEAKLY_ASCENDING:
        return 'WEAKLY ASCENDING'
    elif FLAG_DESCENDING:
        return 'DESCENDING'
    elif FLAG_WEAKLY_DESCENDING:
        return 'WEAKLY DESCENDING'
    else:
        return 'RANDOM'
    
print(answer())