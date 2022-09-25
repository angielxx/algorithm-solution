
T = 10

for tc in range(1, T+1):
    N, numbers = input().split()
    N = int(N)

    num_list = []
    for i in range(N):
        num_list.append(int(numbers[i]))

    # 괄호 검사와 같은 원리
    stack = []
    for i in range(N):
        if stack:
            if stack[-1] == num_list[i]:
                stack.pop()
            else:
                stack.append(num_list[i])
        else:
            stack.append(num_list[i])

    print('#{}'.format(tc), end=' ')
    while stack:
        n = stack.pop(0)
        print(n, end='')
    print()