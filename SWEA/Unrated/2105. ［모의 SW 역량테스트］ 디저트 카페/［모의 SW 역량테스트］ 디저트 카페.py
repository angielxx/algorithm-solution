T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    move = [[-1,-1],[1,1],[-1,1],[1,-1]]

    max_cnt = 0
    # dir는 k를 저장한다. (꺾일때만)
    # path에는 (i, j)를 저장한다.
    def dfs(i, j, cnt=0, dir=[], path=[], cake=[]):
        global max_cnt
        si, sj = i, j

        for k in range(4):
            ni, nj = si + move[k][0], sj + move[k][1]
            if 0 <= ni < N and 0 <= nj < N:
                # 도착 지점일 때 (직선으로 도착한 경우도 있음..)
                if dir and (ni, nj) == path[0] and cnt >= 4:
                    if max_cnt < cnt:
                        # print(path)
                        # print(cake)
                        max_cnt = cnt
                    return

                # 도착 지점이 아닐 때 전진
                else:
                    # 케이크 종류 먼저 확인
                    if arr[ni][nj] not in cake:
                        # 직선 이동인 경우
                        if dir and k == dir[-1]:
                            dfs(ni, nj, cnt + 1, dir, path + [(ni, nj)], cake + [arr[ni][nj]])
                        # 직각 이동인 경우(출발지점이거나 직각이동)
                        elif not dir or k not in dir:
                            dfs(ni, nj, cnt + 1, dir + [k], path + [(ni, nj)], cake + [arr[ni][nj]])

    for i in range(N):
        for j in range(N):
            dfs(i, j)
    if max_cnt == 0:
        max_cnt = -1
    print('#{}' .format(tc), max_cnt)