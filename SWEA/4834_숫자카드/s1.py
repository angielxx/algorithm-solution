# SWEA 4834 숫자카드
# 220809

import sys

sys.stdin = open('sample_input.txt' , 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 카운트 리스트
    c = [0] * 10

    # 각 숫자 인덱스에 +1
    for num in map(int, input()):
        c[num] += 1

    # 제일 큰 수와 그 인덱스 찾기
    max_val = 0
    max_idx = 0
    for idx in range(10):
        if c[idx] >= max_val:
            max_val = c[idx]
            max_idx = idx
    print('#{} {} {}' .format(tc, max_idx, max_val))