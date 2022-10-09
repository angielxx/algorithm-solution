# BOJ 1697 숨바꼭질
# 221009

import collections
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())

MAX = 10**5
count = [INF] * (MAX + 1)
count[N] = 0

Q = collections.deque()
Q.append(N)

cnt = 0
while Q:
    x = Q.popleft()
    if x == K:
        cnt += 1
    
    for nx in (x + 1, x - 1, x * 2):
        if 0 <= nx <= MAX and count[x] + 1 <= count[nx]:
            count[nx] = count[x] + 1
            Q.append(nx)
print(count[K])
print(cnt)