import sys
input = sys.stdin.readline

t = int(input())

dp = [0] * 13
dp[1] = 1
dp[2] = 2
dp[3] = 4


for i in range(4, 13):
    total = 0
    total += dp[i - 1]
    total += dp[i - 2]
    total += dp[i - 3]
    dp[i] = total
    
for _ in range(t):
    print(dp[int(input())])