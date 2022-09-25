T = 10

for tc in range(1, T+1):
    N = int(input())
    infix = input()

    # stack1 = []
    # i부터 N까지
    def cal(i, N):
        # 여는 괄호 만날 때마다 새로운 스택 생성
        # 한 괄호에 대해 연산하려고 하는 숫자 저장
        stack = []
        # 한 괄호에 대한 총 연산값
        total = 0
        while True:
            if i == N:
                total = stack.pop()
                while stack:
                    total *= stack.pop()
                return total
            else:
                # 숫자는 일단 넣기
                if infix[i].isnumeric():
                    stack.append(int(infix[i]))
                    i += 1
                # 곱셈을 만나면 숫자를 지나간다 (다음 숫자도 곱할 값으로 스택에 저장)
                elif infix[i] == '*':
                    i += 1
                    pass
                # 곱셈을 만나면 스택에 저장된 숫자를 모두 곱한다.
                elif infix[i] == '+':
                    temp = stack.pop()
                    while stack:
                        temp *= stack.pop()
                    # 곱한 값을 총 연산값에 더한다.
                    total += temp
                    i += 1
                # 또 여는 괄호를 만나면 괄호 안을 모두 연산한 값을 받아서 스택에 저장
                elif infix[i] == '(':
                    temp, next_i = cal(i+1, N)
                    i = next_i
                    stack.append(temp)
                # 닫는 괄호를 만나면 스택에 있는 모든 숫자를 곱해서 더하고 종료
                elif infix[i] == ')':
                    temp = stack.pop()
                    while stack:
                        temp *= stack.pop()
                    total += temp
                    # 괄호에 대한 연산값을 반환
                    # 다음으로 봐야할 i번째도 반환
                    return total, i+1

    print('#{}' .format(tc), cal(0, N))