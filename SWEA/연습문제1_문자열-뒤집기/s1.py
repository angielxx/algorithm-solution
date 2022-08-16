# 연습문제1_문자열 뒤집기
# 220812

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    s = input()

    result = s[::-1]

    print('#{} {}' .format(tc, result))