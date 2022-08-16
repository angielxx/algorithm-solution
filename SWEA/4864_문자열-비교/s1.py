# SWEA 4864_문자열 비교
# 220816

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    N, M = len(str1), len(str2)

    cnt = 0
    for i in range(M-N+1):
        if str2[i:i+N] == str1:
            cnt += 1

    print('#{} {}' .format(tc, cnt))