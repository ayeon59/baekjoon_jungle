m = int(input())
line = []

# 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    line.append((a, b))
    
line.sort()
b_values = [b for a, b in line]
dp = [1] * m

for i in range(1, m):
    for j in range(i):
        if b_values[i] > b_values[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(m - max(dp))
