from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 결과 저장용 배열
result = [[0] * n for _ in range(n)]


for i in range(n):
    visited = [False] * n
    q = deque()
    q.append(i)

    while q :
        cur = q.popleft()
        for next in range(n):
            if not visited[next] and graph[cur][next] :
                visited[next] = 1
                result[i][next] = 1
                q.append(next)

for row in result:
    print(' '.join(map(str, row)))
