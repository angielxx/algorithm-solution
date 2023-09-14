import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
cnt = 0
for i in range(n - 2, -1, -1):
    k = i + 1
    while k < n:
        cnt += 1
        if arr[i] < arr[k]:
            dp[i] = max(dp[i], dp[k] + 1)
        k += 1
print(max(dp))