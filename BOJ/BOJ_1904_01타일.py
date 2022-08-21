# BOJ 1904 01타일
# 220820

# 메모이제이션 : 메모리초과

import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[N])