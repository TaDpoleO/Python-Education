inp_file = open('input.txt')

N = int(inp_file.readline())
F = []
F.append((float(inp_file.readline()), ''))
for _ in range(N-1):
    curr_F = inp_file.readline().split()
    F.append((float(curr_F[0]), curr_F[1]))
    
def answer(F):
    Fmin, Fmax = 30, 4000
    
    prev_F = F[0][0]
    for curr_F, state in F[1:]:
        mid_F = (curr_F+prev_F)/2
        if state == 'closer':
            if curr_F < prev_F:
                Fmax = min(Fmax, mid_F)
            elif curr_F > prev_F:
                Fmin = max(Fmin, mid_F)
        elif state == 'further':
            if curr_F < prev_F:
                Fmin = max(Fmin, mid_F)
            elif curr_F > prev_F:
                Fmax = min(Fmax, mid_F)
            
        prev_F = curr_F
        
    
    return Fmin, Fmax
    
print(*answer(F))