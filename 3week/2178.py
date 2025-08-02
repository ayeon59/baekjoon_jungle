import sys
from collections import deque
sys.setrecursionlimit(10000)  
input = sys.stdin.readline

n,m = map(int,input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while queue :
        cx,cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m :
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[cx][cy] + 1
                    queue.append((nx, ny))


queue = deque([(0,0)])
bfs()
print(maze[n-1][m-1])










# def dfs(x,y,count):
#     global min_count
#     visited[x][y] = True
#     if count > min_count :
#         return
#     if x==n-1 and y == m-1 :
#         min_count = min(min_count,count)
#         return 
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx< n and 0<=ny<m :
#             if not visited[nx][ny] and maze[nx][ny] == 1:
#                 dfs(nx,ny,count+1)
#                 visited[nx][ny] = False
    
            

# visited = [[False]*m for _ in range(n)]
# dfs(0,0,1)
# print(min_count)

