# n = int(input())
# dp = [[0]*(n+1) for _ in range(n//2+1)]

# # 첫 번째 열 초기화
# for i in range(n//2+1):
#     dp[i][0] = 1

# for j in range(n+1):
#     dp[0][j] = 1

# sum = 0
# for i in range(n//2+1):
#     for j in range(n+1):
#         if i != 0 and j != 0 :
#             dp[i][j] = dp[i][j-1] + dp[i-1][j]
#         if i*2 + j == n :
#             sum += dp[i][j]

# print(sum%15746)


n = int(input())
dp = [0] * (n + 2)  
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])
