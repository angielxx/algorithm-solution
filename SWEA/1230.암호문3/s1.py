# 1230.
# 220826

import sys
sys.stdin = open('input.txt', 'r')
# sys.stdin = open('test.txt', 'r')

T = 10

def insert(x, y, s):
    global pw, N

    temp = []
    for _ in range(x+1):
        temp.append(pw.pop(0))
    temp += s
    temp += pw
    pw = temp
    N += y
    return

def delete(x, y):
    global pw, N

    temp = []
    for _ in range(x+1):
        temp.append(pw.pop(0))
    for _ in range(y):
        pw.pop(0)
    temp += pw
    pw = temp
    N -= y
    return

def add(y, s):
    global pw, N
    pw += s
    N += y

for tc in range(1, T+1):
    N = int(input())
    pw = list(map(int, input().split()))
    M = int(input())
    cm = list(input().split())

    cm_list = []
    stack = []
    while cm:
        # temp = cm.pop(0)
        # print(temp, stack)
        # 알파벳이긴한데 스택에 아무것도 없을 때
        if cm[0].isalpha() and not stack:
            stack.append(cm.pop(0))
        elif cm[0].isnumeric():
            stack.append(int(cm.pop(0)))
        elif not cm or cm[0].isalpha() and stack:
            # print(stack)
            if stack[0] == 'I':
                insert(stack[1], stack[2], stack[3:])
            elif stack[0] == 'D':
                delete(stack[1], stack[2])
            elif stack[0] == 'A':
                add(stack[1], stack[2:])
            stack.clear()
    if stack:
        if stack[0] == 'I':
            insert(stack[1], stack[2], stack[3:])
        elif stack[0] == 'D':
            delete(stack[1], stack[2])
        elif stack[0] == 'A':
            add(stack[1], stack[2:])
        stack.clear()

    print('#{}' .format(tc), *pw[1:11])