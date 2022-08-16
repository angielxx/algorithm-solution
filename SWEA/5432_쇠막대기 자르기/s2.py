# SWEA 5432. 쇠막대기 자르기
# 220816

# Fail (제한시간 초과)

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str = input()

    length = 0
    for s in str:
        length += 1

    # 임시 스택
    stack = []
    # 짝이 되는 괄호의 인덱스를 튜플로 저장
    pair = []

    for i in range(length):
        if str[i] == '(':
            stack.append(i)
        if str[i] == ')':
            pair.append( (stack.pop(), i) )
            stack.
    # 레이저
    lazer = []
    # 막대
    stick = []
    for tuple in pair:
        if tuple[0] + 1 == tuple[1]:
            lazer.append(tuple)
        else:
            stick.append(tuple)

    # stick 순회하며 막대기 범위 안에 있는 레이저 갯수 세기
    cnt = 0
    for tuple1 in stick:
        start, end = tuple1
        # 잘리지 않은 상태 1개
        cnt += 1
        for tuple2 in lazer:
            s, e = tuple2
            if s > start and e < end:
                cnt += 1

    print('#{} {}' .format(tc, cnt))
