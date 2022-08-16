# SWEA 2001. 파리 퇴치 D2
# 220816

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    arr= [list(map(int, input().split())) for _ in range(N)]

    di = []
    for k in range(M):
        for _ in range(M):
            di.append(k)
    dj = []
    for _ in range(M):
        for k in range(M):
            dj.append(0 + k)

    max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for k in range(M*M):
                ni = i + di[k]
                nj = j + dj[k]
                s += arr[ni][nj]
            if s >= max:
                max = s

    print('#{} {}' .format(tc, max))