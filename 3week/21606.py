import sys
sys.setrecursionlimit(10000)  
input = sys.stdin.readline

n = int(input())
place = input()
take_walk = [[] for _ in range(n+1)]
count = 0

for i in range(n-1):
    a, b = map(int,input().split())
    take_walk[a].append(b)
    take_walk[b].append(a) 

def dfs(next):
    global count
    for neighbor in take_walk[next]:
        if visited[neighbor]:
            continue
        if int(place[neighbor-1]) == 1:
            count += 1
            continue
        visited[next] = True
        dfs(neighbor)

for i in range(1,n+1):
    #실내장소에서 출발
    if int(place[i-1]) == 1:
        visited = [False] * (n+1)
        visited[i] = True
        dfs(i)
print(count)



# import sys
# input = sys.stdin.readline
# from itertools import permutations
# sys.setrecursionlimit(10**6)

# n = int(input())
# place = input().strip()
# graph = [[] for _ in range(n + 1)]

# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# visited = [False] * (n + 1)
# answer = 0

# def dfs(node):
#     visited[node] = True
#     if place[node - 1] == '1':  # 내부 노드면 리스트에 포함
#         return [node]
    
#     total = []
#     for neighbor in graph[node]:
#         if not visited[neighbor]:
#             result = dfs(neighbor)
#             total += result
    
#     # 외부 노드 기준으로 연결된 내부 노드들로 순서쌍 계산
#     global answer
#     answer += len(list(pe-rmutations(total, 2)))
#     return []


# for a in range(1, n + 1):
#     for b in graph[a]:
#         if a < b and place[a - 1] == '1' and place[b - 1] == '1':
#             answer += 2


# for i in range(1, n + 1):
#     if not visited[i] and place[i - 1] == '0':
#         dfs(i)

# print(answer)





# import sys
# from itertools import permutations
# input = sys.stdin.readline

# n = int(input())
# place = input()
# take_walk = [[] for _ in range(n+1)]
# # visited_master = [False] * (n+1) 
# stack = []
# count = 0

# for i in range(n) :
#     if int(place[i]) == 0:
#         stack.append(i+1)

# for i in range(n-1):
#     a, b = map(int,input().split())
#     #내부끼리 연결하는 개수
#     if int(place[a-1]) == 1 and int(place[b-1]) == 1 :
#         count += 2
#     take_walk[a].append(b)
#     take_walk[b].append(a) 

# while stack :
#     in_now = stack.pop()
#     internal_neighbors = [x for x in take_walk[in_now] if int(place[x-1]) == 1]
#     count += len(list(permutations(internal_neighbors,2))) 

# print(count)


# # def dfs(next):
# #     global count
# #     visited[next] = True
# #     for neighbor in take_walk[next]:
# #         if visited[neighbor]:
# #             continue
# #         if int(place[neighbor-1]) == 1:
            
# #             count += 1
# #             continue
# #         dfs(neighbor)

# # for i in range(1,n+1):
# #     if visited_master
# #     #실내장소에서 출발
# #     visited = [False] * (n+1)
# #     #애초에 실외장소에서 출발하는거 컷
# #     if int(place[i-1]) == 1:
# #         dfs(i)
# # print(count)


# for i in range(n):
#     if int(place[i]) == 0 :
#         print("*")
#         count += len(list(permutations(take_walk[i+1],2)))
#     else :
#         out.append(i+1)

# for i in range(n):
#     if int(place[i]) == 1 :
#         for x in out :
#             if x in take_walk[i+1]:
#                 break
#         count += 1



# print(count)

