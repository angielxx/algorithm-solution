# SWEA 5188 최소합
# 220921

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    delta = [[-1,0],[1,0],[0,-1],[0,1]]

    # 출발 지점
    si, sj = 0, 0
    # 도착 지점
    E = (N-1, N-1)

    min_sum = 10*13
    def dfs(start, path, path_sum):
        global min_sum
        if path_sum >= min_sum:
            return
        si, sj = start
        if si == N-1 and sj == N-1:
            print(path_sum, path)
            if path_sum < min_sum:
                min_sum = path_sum
            return
        
        stack = []
        for k in range(4):
            ni, nj = si + delta[k][0], sj + delta[k][1]
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in path:
                stack.append((ni, nj))
        stack.sort(reverse=True, key=lambda x : arr[x[0]][x[1]])
        while stack:
            ni, nj = stack.pop()
            # path 보낼 때 path.append로 추가해서 보내주니 얕은 복사됨
            dfs((ni, nj), path + [(ni, nj)], path_sum + arr[ni][nj])
        
    
    dfs((si, sj), [(si, sj)], arr[si][sj])
    print('#{}' .format(tc), min_sum)
        
