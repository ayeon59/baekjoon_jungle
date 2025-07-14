from itertools import permutations

n = int(input())
a = list(map(int,input().split()))
max = 0
sum = 0
for perm in permutations(a,len(a)):
    perm = list(perm)
    for i in range(n-1):
        sum += abs(perm[i] - perm[i+1])
        
        
    if sum >= max : max = sum
    sum = 0


print(max)
    
