# SWEA 3143. 가장 빠른 문자열 타이핑
# 220816

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    # A의 길이
    N = 0
    for s in A:
        N += 1

    # B의 길이
    M = 0
    for s in B:
        M += 1

    # 타이핑 횟수
    cnt = 0

    i = 0
    while i < N:
        cnt += 1
        if A[i:i+M] == B:
            i += M
        else:
            i += 1

    print('#{} {}' .format(tc, cnt))
