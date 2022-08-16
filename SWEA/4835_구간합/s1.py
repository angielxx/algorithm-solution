# SWEA 4835 구간합
# 220809

import sys

sys.stdin = open('sample_input.txt' , 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 인풋받아 num_list에 저장
    num_list = list(map(int, input().split()))

    # 모든 경우의 합들을 저장할 sum_list 생성
    sum_list = list()
    # 구간별 첫번째 숫자
    for i in range(N - M + 1): # 0 ~ 7
        sum = 0
        # 반복해서 더할 횟수 = 구간의 길이
        for j in range(M): # 0 1 2
            sum += num_list[i + j]
        sum_list.append(sum)
    
    # 최대 합과 최소 합 찾기
    min = max = sum_list[0]
    for sum in sum_list:
        if sum >= max:
            max = sum
        if sum <= min:
            min = sum

    print('#{} {}' .format(tc, max - min))