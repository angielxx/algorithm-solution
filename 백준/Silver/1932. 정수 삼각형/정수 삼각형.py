import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * i for i in range(1, n + 1)]

dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] = dp[i - 1][-1] + triangle[i][j]
        else:
            left = dp[i-1][j-1] + triangle[i][j]
            right = dp[i-1][j] + triangle[i][j]
            dp[i][j] = max(left, right)
            
print(max(dp[n-1]))