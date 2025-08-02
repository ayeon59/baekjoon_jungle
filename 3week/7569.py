import sys
from collections import deque

n, m , h = map(int,input().split())
tomato = []
# print(arr[1][1][2])
# 층, 행, 열
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
visited = [[[False for _ in range(n)] for _ in range(m)] for _ in range(h)]

queue = deque()

for _ in range(h):
    layer = []
    for _ in range(m):
        row = list(map(int, input().split()))
        layer.append(row)
    tomato.append(layer)

is_rippen = False
for k in range(h):
    for i in range(m):
        for j in range(n):
            if tomato[k][i][j] == 1 :
                visited[k][i][j] = True
                queue.append((k,i,j))
            if tomato[k][i][j] == 0 :
                is_rippen = True

if not is_rippen :
    print(0)
    sys.exit()

while queue :
    now_z, now_y, now_x = queue.popleft()
    for i in range(6):
        next_z = now_z + dz[i]
        next_y= now_y + dy[i]
        next_x = now_x + dx[i]
        if 0<=next_z<h and 0<=next_y<m and 0<=next_x<n :
            if not visited[next_z][next_y][next_x] :
                if tomato[next_z][next_y][next_x] == 0:
                    visited[next_z][next_y][next_x] = True
                    tomato[next_z][next_y][next_x] = tomato[now_z][now_y][now_x] + 1
                    queue.append((next_z,next_y,next_x))




has_zero = any(0 in row for layer in tomato for row in layer)
if has_zero :
    print(-1)
else :
    max_day = max(max(max(row) for row in layer) for layer in tomato)
    print(max_day - 1)

