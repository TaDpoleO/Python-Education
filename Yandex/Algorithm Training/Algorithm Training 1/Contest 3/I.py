from functools import reduce

inp_file = open('input.txt')
N = int(inp_file.readline())

scholars, languages = [0]*N, set()
for i in range(N):
   M = int(inp_file.readline())
   scholars[i] = set()
   for _ in range(M):
       lang = inp_file.readline().rstrip()
       languages.add(lang)
       scholars[i].add(lang)
      
res = reduce(set.intersection, scholars)
print(len(res))
print(*res, sep='\n')
print(len(languages))
print(*languages, sep='\n')