import sys
input = sys.stdin.readline

num = input().strip()
n = len(num)

if int(num) == 0:
    print(0)
elif 1 <= int(num) < 10:
    print(1)
else:

    dp = [1] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] # 1,2,3,5,8,13...

    answer = 1
    temp = 0
    for i in range(n):
        if i == 0 and int(num[i]) == 0:
            answer = 0
            break
        if int(num[i]) == 0 and int(num[i-1]) > 2:
            answer = 0
            break
        if i + 1 < n and int(num[i]) == 0 and int(num[i + 1]) == 0:
            answer = 0
            break

        if int(num[i]) == 0:
            temp = max(temp - 1, 0)
            answer *= dp[temp]
            temp = 0
        elif int(num[i:i+2]) <= 26:
            temp += 1
        else:
            temp += 1
            answer *= dp[temp]
            temp = 0

    answer *= dp[temp]
    print(answer % 1000000)
