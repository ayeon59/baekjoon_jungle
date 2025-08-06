# t = int(input())

# for _ in range(t):
#     n = int(input())
#     coins = list(map(int, input().split()))
#     total = int(input())

#     dp = [0] * (total + 1)
#     dp[0] = 1  

#     for coin in coins:
#         for j in range(coin, total + 1):
#             dp[j] += dp[j - coin]

#     print(dp[total])


t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    total = int(input())

    dp = [[0] * (total + 1) for _ in range(n)]

    
for j in range(0, total + 1):
    if j % coins[0] == 0:
        dp[0][j] = 1


for i in range(1, n):
    for j in range(total + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= coins[i]:
            dp[i][j] += dp[i][j - coins[i]]

print(dp[n - 1][total])

