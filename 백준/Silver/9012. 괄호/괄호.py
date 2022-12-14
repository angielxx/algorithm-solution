import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    string = input().strip()
    stack = []
    flag = True
    for s in string:
        # print(stack)
        # print(s, flag)
        if s == '(':
            stack.append(s)
        else:
            if stack and (stack[-1] == '('):
                stack.pop()
            else:
                flag = False
    # print('hi', flag)
    if (len(stack)): flag = False

    if (flag): print('YES')
    else: print('NO')