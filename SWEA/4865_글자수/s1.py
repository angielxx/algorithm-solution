# SWEA 4865_글자수
# 220816

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    # 딕셔너리 만들기
    # key : val = 알파벳 : [ 발견하면 저장 ]
    alpha = dict()
    str1 = list(set(str1))
    for s in str1:
        alpha[s] = []
    for i in range(len(str2)):
        s = str2[i]
        if s in alpha.keys():
            alpha[s].append(s)

    # 가장 많은 글자의 개수
    max = 0
    for val in alpha.values():
        length = 0
        while val:
            length += 1
            val.pop()
        if length >= max:
            max = length
    print('#{} {}' .format(tc, max))
