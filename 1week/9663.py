n = int(input())
count = 0

def dfs(x, y, step):
    global count
    if step == n:
        count += 1
        return

    for i in range(n):
        for j in range(n):
            if i != x and j != y and x + y != i + j and y - x != j - i:
                dfs(i, j, step + 1)

for i in range(n):
    for j in range(n):
        dfs(i, j, 0)

print(count)
