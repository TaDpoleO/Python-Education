fin = open('input.txt')
S = fin.readline().rstrip()

N = len(S)
x0 = 277
p = 1073676287

prefix = [0]*(N+1)
prefix_rev = [0]*(N+1)
x = [1]*(N+1)

for i in range(N):
    prefix[i+1] = (prefix[i]*x0+ord(S[i])) % p
    prefix_rev[i+1] = (prefix_rev[i]*x0+ord(S[N-i-1])) % p
    x[i+1] = (x[i]*x0) % p

# index = 0...N-1
def isPalindrome(pos, slen):    
    return (prefix[pos+slen]+prefix_rev[N-pos-slen]*x[slen]) % p == (prefix_rev[N-pos]+prefix[pos]*x[slen]) % p

def check_odd(radius, center):
    return isPalindrome(center-radius, 1+2*radius)

def check_even(radius, center):
    return isPalindrome(center+1-radius, 2*radius) 

def bsearch(left, right, check, check_param):
    while left < right:
        # mid - radius of palindrome
        mid = (left+right+1)//2
        # TTFF, TTTT        
        if check(mid, *check_param):
            left = mid
        else:
            right = mid-1

    return left

odd_palindrome_counter = 0
even_palindrome_counter = 0

for i in range(N):
    odd_palindrome_counter += bsearch(0, min(i, N-i-1), check_odd, [i])+1
    even_palindrome_counter += bsearch(0, min(i+1, N-1-i), check_even, [i])

print(odd_palindrome_counter+even_palindrome_counter)