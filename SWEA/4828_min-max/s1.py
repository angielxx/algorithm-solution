# SWEA 4828 min-max
# 220809

import sys

sys.stdin = open('sample_input.txt' , 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    # 양의 정수들 저장할 리스트
    # N개의 양의 정수 저장
    num_list = list(map(int, input().split()))

    # num_list의 첫번째 원소로 초기화
    min = max = num_list[0]

    # 초기화 숫자와 비교하며 min, max 갱신
    for num in num_list:
        if num >= max:
            max = num
        if num <= min:
            min = num

    print('#{} {}' .format(tc, max-min))