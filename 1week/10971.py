def dfs(city, visited, cost, start):
    global min_cost

    if visited.count(0) == 0:
        if city_move[city][start] == 0:
            return
        cost += city_move[city][start]
        min_cost = min(min_cost, cost)
        return

    for i in range(n):
        if visited[i] == 1 or city_move[city][i] == 0:
            continue
        visited[i] = 1
        dfs(i, visited, cost + city_move[city][i], start)
        visited[i] = 0



n = int(input())
city_move = [list(map(int, input().split())) for _ in range(n)]
min_cost = float('inf')


for i in range(n):
    visited = [0] * n
    visited[i] = 1
    dfs(i, visited, 0, i)

# 정답 출력
print(min_cost)
