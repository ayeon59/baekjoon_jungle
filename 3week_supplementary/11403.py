#인접행렬문제
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

#k번을 거쳐 가는 경우 전부 카운트
#k+1번을 거쳐 가는 경우 전부 카운트
#visited 를 안쓰는 이유? k번째를 거쳐감으로써 발생하는 새로운 루트에서 뻗어나가는 탐색 기회를 놓치게 됨
for k in range(n):         # 거쳐가는 노드
    for i in range(n):     # 시작 노드
        for j in range(n): # 도착 노드
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for row in graph:
    print(*row)



# #A->B B->C 까지밖에 탐색 안하고 C->D를 못함
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             #현재 탐색 할 노드가 이미 방문한 노드면 확인하지 않음
#             if visited[i][j] : continue
#             #갈 수 있는 노드면 올 수도 있음
#             if graph[i][j] == 1 :
#                 graph[j][i] = 1
#                 visited[j][i] = 1
            
#             if graph[i][j] == 1 and graph[j][k] == 1 and not visited[i][k]:
#                 graph[i][k] = 1
#                 visited[i][k] = 1
#                 graph[k][i] = 1
#                 visited[k][i] = 1
        
