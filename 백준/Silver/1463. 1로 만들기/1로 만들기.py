import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 2)
dp[2] = 1

for i in range(3, n+2):
    a = dp[i - 1] + 1
    if i % 3 == 0:
        b = dp[i // 3] + 1
    if i % 2 == 0:
        c = dp[i // 2] + 1
    
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(a, b, c)
    elif i % 3 == 0 and i % 2 != 0:
        dp[i] = min(a, b)
    elif i % 3 != 0 and i % 2 == 0:
        dp[i] = min(a, c)
    else:
        dp[i] = a
    
print(dp[n])