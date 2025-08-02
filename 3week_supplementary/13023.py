n, m = map(int,input().split())
visited = [False] * n
friend = [] 
for _ in range(n):
    a, b =map(int,input().split())
    friend.append((a,b))
