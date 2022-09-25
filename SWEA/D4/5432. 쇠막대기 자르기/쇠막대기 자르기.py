
T = int(input())

for tc in range(1, T+1):
    str = input()

    # 현재 막대기의 개수
    stick = 0
    # 최종 막대기의 개수
    result = 0

    i = 0
    while i < len(str):
        # 레이저의 (를 만나면 현재 막대기 개수만큼 총개수 증가, i += 2
        if str[i] == '(' and str[i+1] == ')':
            result += stick
            i += 2
        # 레이저가 아닌 (
        elif str[i] == '(':
            stick += 1
            i += 1
        # )를 만나면 총 개수 +1
        else:
            result += 1
            stick -= 1
            i += 1

    print('#{} {}' .format(tc, result))