T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split()) # 5, 2

    cases = list()
    for n in range(N):
        cases.append(list(map(int, input().split())))

    sum_list = list()
    for i in range(N - M +1): # (0,4) = 0,1,2,3
        for j in range(N - M + 1): # 0,1,2,3
            sum = 0
            for k in range(M): # 0,1
                for l in range(M):
                    sum += cases[i + k][j + l]
            sum_list.append(sum)
    sum_list.sort(reverse = True)
    print(f'#{t} {sum_list[0]}')