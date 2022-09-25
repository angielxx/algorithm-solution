
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    days = list(map(int, input().split()))

    # 최종 이익
    margin = 0

    # 범위 시작과 끝 idx
    start = -1
    end = -1
    while start < N - 1:
        max = 0
        for i in range(end+1, N):
            if days[i] > max:
                max = days[i]
                end = i

        for j in range(start+1, end):
            margin += (max - days[j])
        temp = end
        start = temp

    print('#{} {}' .format(tc, margin))
