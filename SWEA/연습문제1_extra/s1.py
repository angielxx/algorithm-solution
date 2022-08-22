# 연습문제1 extra
# 220822

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

isp = {'*':2, '/':2, '+':1, '-':1, '(':0}
icp = {'*':2, '/':2, '+':1, '-':1, '(':3}

for tc in range(1, T+1):
    infix = input()

    postfix = []
    stack = []
    length = 0
    for s in infix:
        length += 1
    # infix 순회
    for i in range(length):
        if infix[i] == '(':
           stack.append(infix[i])
        elif infix[i].isnumeric():
            postfix.append(infix[i])
        elif infix[i] == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            if stack:
                if isp[stack[-1]] < icp[infix[i]]:
                        stack.append(infix[i])
                else:
                    while stack and isp[stack[-1]] >= icp[infix[i]]:
                        postfix.append(stack.pop())
                    stack.append(infix[i])
            else:
                stack.append(infix[i])
    while stack:
        postfix.append(stack.pop())
    print('#{}' .format(tc), ''.join(postfix))