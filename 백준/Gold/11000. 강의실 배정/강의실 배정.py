# BOJ 11000 강의실 배정
# 221011

import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

Q = []
heapq.heappush(Q, arr[0][1])
for i in range(1, N):
    s, e = arr[i]
    if s < Q[0]:
        heapq.heappush(Q, e)
    else:
        heapq.heappop(Q)
        heapq.heappush(Q, e)

print(len(Q))