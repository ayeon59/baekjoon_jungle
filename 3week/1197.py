
import sys, heapq
input = sys.stdin.readline

v, e = map(int,input().split())
visited = [False] * (v+1)
graph = [[] for _ in range(v+1)]
heap = []
total_weight = 0

def prim(start):
    global total_weight
    for edge in graph[start]:
        heapq.heappush(heap,edge)
        
    while heap :
        weight, next_node= heapq.heappop(heap)
        if not visited[next_node] :
            visited[next_node] = True
            total_weight += weight
            for edge in graph[next_node]:
                if not visited[edge[1]] :
                    heapq.heappush(heap,edge)

for _ in range(e):
    a,b,weight = map(int,input().split())
    graph[a].append((weight,b))
    graph[b].append((weight,a))    
visited[1] = True
prim(1)
print(total_weight)









# v, e = map(int,input().split())
# graph = [[] for _ in range(v + 1)]
# sum_node = 0
# count = 0
# def dfs(start) :
#     global sum_node, count
#     if count > v-1 :
#         return
#     count += 1
#     next = min(graph[start], key=lambda x: x[-1])
#     next_node, next_weight = next[0],next[1]
#     sum_node += next_weight
#     dfs(next_node)

# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     graph[a].append((b, cost))
#     graph[b].append((a, cost))  
    
# dfs(1)

# print(sum_node)

