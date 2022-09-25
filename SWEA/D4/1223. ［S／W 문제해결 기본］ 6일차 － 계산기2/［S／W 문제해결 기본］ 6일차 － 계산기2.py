
T = 10

for tc in range(1, T+1):
    N = int(input())
    infix = input()

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