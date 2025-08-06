n, m = map(int,input().split())
stone = [True] * (n+1) 
visited = [False] * (n+1) 
min_step = 10**6
dx = [-1,0,1]
for _ in range(m):
    a = int(input())
    stone[a] = False

def dfs(target,step,cnt):
    global min_step
    
    if target >= n :
        if target == n :
            min_step = min(min_step,cnt)
        return
    for i in range(3):
        if step + dx[i] < 1 :
            continue    
        nx = target + step + dx[i]
        if nx <= n :
            if not visited[nx] and stone[nx]:
                visited[nx] = True
                dfs(nx,step+dx[i],cnt+1)
                visited[nx] = False
        



dfs(1,1,0)
print(min_step)