import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
maze = [list(map(int, list(input().strip()))) for _ in range(n)]

INF = 10**9
dist = [[INF]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
dq.append((0, 0))
dist[0][0] = 0

while dq:
    x, y = dq.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            cost = dist[x][y] + (1 if maze[nx][ny] == 0 else 0)

            if cost < dist[nx][ny]:
                dist[nx][ny] = cost
                if maze[nx][ny] == 1:
                    dq.appendleft((nx, ny))
                else:
                    dq.append((nx, ny))

print(dist[n-1][n-1])