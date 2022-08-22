# 연습문제1 후위표기법
# 220822

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

priority = { '*':3, '/':3, '+':2, '-':2, '(':1 }

for tc in range(1, T+1):
    infix = input()

    postfix = []
    stack = []

    # 길이 구하기
    length = 0
    for x in infix:
        length += 1

    # 입력값 순회
    for i in range(length):
        if infix[i].isalnum():
            postfix.append(infix[i])
        else:
            stack.append(infix[i])

    while stack:
        postfix.append(stack.pop())

    print('#{}' .format(tc), ''.join(postfix))
