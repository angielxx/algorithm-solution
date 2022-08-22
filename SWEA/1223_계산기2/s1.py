# SWEA 1223. 계산기2
# 220822

import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    infix = sys.stdin.readline()

    stack = []
    total = 0
    for i in range(N):
        if infix[i] == '+':
            temp = stack.pop()
            while stack:
                temp *= stack.pop()
            total += temp
        elif infix[i] == '*':
            pass
        elif infix[i].isnumeric():
            stack.append(int(infix[i]))
    if stack:
        temp = stack.pop()
        while stack:
            temp *= stack.pop()
        total += temp
    print('#{} {}' .format(tc, total))

