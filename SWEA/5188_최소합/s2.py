# SWEA 5188 최소합
# 220922

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 출발지점, 도착지점
    si, sj = 0, 0
    ei, ej = N-1, N-1

    # 델타 탐색 : 하우
    delta = [[1,0],[0,1]]

    min_sum = 10 * 130

    # path에는 (i, j)로 저장
    def bfs(si, sj, path=[], path_sum=0):
        global min_sum

        temp_path = path[:]
        temp_path.append((si, sj))
        path_sum += arr[si][sj]  

        # 넘어버리면 종료
        if path_sum > min_sum:
            return

        # 도착지점인지 확인
        if si == ei and sj == ej:
            if path_sum < min_sum:
                min_sum = path_sum
            return

        # 델타 탐색
        # moveTo = []
        for k in range(2):
            ni, nj = si + delta[k][0], sj + delta[k][1]
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in temp_path:
                bfs(ni, nj, temp_path, path_sum)

    bfs(si, sj, [], 0)
    print('#{}' .format(tc), min_sum)