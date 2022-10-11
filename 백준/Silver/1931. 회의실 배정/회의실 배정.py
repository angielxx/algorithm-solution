# BOJ 1931 회의실 배정
# 221011

# 빨리 끝나는 애부터 골라야 그 이후에 고를 수 있는 회의의 수를 최대로 가져갈 수 있다
# 시작 시간은 빠른애가 먼저 와야한다.

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))

cnt = 1
s, e = arr[0]
for i in range(1, N):
    ns, ne = arr[i]
    if e <= ns:
        cnt += 1
        s, e = ns, ne
    else:
        pass

print(cnt)