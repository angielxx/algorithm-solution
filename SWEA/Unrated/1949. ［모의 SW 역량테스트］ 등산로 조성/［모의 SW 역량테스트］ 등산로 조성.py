# SWEA 1949 등산로 조성
# 220925

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    delta = [[1,0],[-1,0],[0,1],[0,-1]]

    max_depth = 0
    def dfs(i, j, depth, visited, flag, before):
        global max_depth
        # print(i, j, depth,visited, flag, before)

        si, sj = i, j
        status = False
        for d in range(4):
            ni, nj = si + delta[d][0], sj + delta[d][1]
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
                if flag:
                    for k in range(1, K+1):
                        if arr[ni][nj] - k < before:
                            status = True
                            dfs(ni, nj, depth + 1, visited + [(ni, nj)], 0, arr[ni][nj] - k)
                if arr[ni][nj] < before:
                    status = True
                    dfs(ni, nj, depth + 1, visited + [(ni, nj)], flag, arr[ni][nj])
        if not status:
            if depth > max_depth:
                # print(visited)
                max_depth = depth
            return
    max_val = 0
    max_li = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_val:
                max_val = arr[i][j]
                max_li = [(i, j)]
            elif arr[i][j] == max_val:
                max_li.append((i, j))
    # print(max_li)
    # print()
    for s in range(len(max_li)):
        i, j = max_li[s][0], max_li[s][1]
        dfs(i, j, 1, [(i, j)], 1, arr[i][j])
    
    print('#{}' .format(tc),max_depth)