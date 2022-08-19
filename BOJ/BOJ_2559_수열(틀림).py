# BOJ 2559 수열
# 220819

# 시간초과
# 예상은 했지만...반복문으로 푸는 문제가 아니다.

import sys
N, K = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

# 0  1  2  3 4 5 6  7 8  9
# 3 -2 -4 -9 0 3 7 13 8 -3
max = 0
for i in range(K):
    max += li[i]

s1 = max
for i in range(N - K - 1):
    s2 = s1
    s2 += li[i+K]
    s2 -= li[i]
    if s2 > max:
        max = s2
    s1 = s2

print(max)