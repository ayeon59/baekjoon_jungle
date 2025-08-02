import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
indegree = [0]*(n+1)
graph = [[] for _ in range(n)]
answer = [0]*(n+1)

for _ in range(n):
    arr.append(list(map(int, input().strip())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            indegree[j] += 1
            graph[i].append(j)

queue = deque()
for i in range(n):
    if indegree[i] == 0:
        queue.append(i)

step = 0
count = 0  # 몇 개의 노드를 정렬했는지
while queue:
    now = queue.popleft()
    step += 1
    count += 1
    answer[now + 1] = step
    for neighbor in graph[now]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

if count != n:
    print(-1)
else:
    for i in range(1, n+1):
        print(answer[i], end=" ")
