# BOJ 1697 숨바꼭질
# 221009

import collections
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())
MAX = 10**5
count = [0] * (MAX+ 1)

Q = collections.deque()
Q.append(N)

while Q:
    x = Q.popleft()

    # 도착
    if x == K:
        print(count[x])
        break

    for nx in (x - 1, x + 1, x * 2):
        # 유효성, 방문 확인
        if 0 <= nx <= MAX and not count[nx]:
            count[nx] = count[x] + 1
            Q.append(nx)