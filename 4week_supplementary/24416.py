import sys
input = sys.stdin.readline

n = int(input())

# 재귀 방식 횟수
count_rec = 0
def fib_recursive(n):
    global count_rec
    if n == 1 or n == 2:
        count_rec += 1
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# DP 방식 횟수
count_dp = 0
def fib_dp(n):
    global count_dp
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        count_dp += 1
    return dp[n]

fib_recursive(n)
fib_dp(n)
print(count_rec, count_dp)
