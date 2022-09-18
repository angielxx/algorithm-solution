# SWEA 1226. 미로1
# 220825

# import sys
# sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 시작점 찾기
    si = sj = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j

    # 상하좌우 델타탐색
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    q = [(si, sj)]
    visited[si][sj] = 1
    status = False
    while q:
        print(visited)
        si, sj = q.pop(0)
        if arr[si][sj] == '3':
            status = True
            break
        else:
            for k in range(4):
                ni, nj = si + di[k], sj + dj[k]
                if 0<= ni <N and 0<= nj < N and arr[ni][nj] != '1' and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[si][sj] + 1
    print(visited)
    # 제일 큰 숫자 찾고 -2
    if status:
        distance = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] > distance:
                    distance = visited[i][j]
        print('#{} {}' .format(tc, distance-2))
    else:
        print('#{}' .format(tc), 0)