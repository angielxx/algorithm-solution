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

    # 레이저의 개수
    lazer = []
    for tuple in pair:
        if tuple[0] + 1 == tuple[1]:
            lazer.append(tuple)

    # 막대기가를 자른 횟수
    result = 0
    # 막대기를 자른 레이저의 개수
    cnt = 0
    for tuple1 in lazer:
        cut = False
        s1, e1 = tuple1
        for tuple2 in pair:
            s2, e2 = tuple2
            if s2 < s1 and e1 < e2:
                cut = True
                result += 1
        if cut:
            cnt += 1
    result += cnt
    print('#{} {}' .format(tc, result))
