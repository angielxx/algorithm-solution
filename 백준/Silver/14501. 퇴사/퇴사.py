import sys
input = sys.stdin.readline

N = int(input())
t = [0] * N
p = [0] * N
dp = [0] * (N+1)

for i in range(N):
    a, b = map(int, input().split())
    t[i], p[i] = a, b

for i in range(N-1, -1, -1):
    if (i + t[i] > N): dp[i] = dp[i + 1]
    else: dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]]) 

print(max(dp))