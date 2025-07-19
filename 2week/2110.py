n, c = map(int,input().split())
c = c-1
home = [int(input()) for _ in range(n)]
home.sort()
gap = 1
max_gap = 0
#가장 뒤에 설치할 와이파이가 범위 안에 있을때까지만
while gap*c <= n-1 :
    min_gap = 10**6
    for i in range(1,c+1):
        min_gap = min(home[gap*i]-home[gap*(i-1)],min_gap)
    max_gap = max(min_gap,max_gap)
    gap += 1
    print(max_gap)
print(max_gap)



