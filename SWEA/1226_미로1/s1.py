# SWEA 1226. 미로1
# 220825

import sys
sys.stdin = open('input.txt', 'r')

T = 10
for _ in range(T):
    tc = int(input())
    arr = [input() for _ in range(16)]

    # 출발지점
    si, sj = 0, 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                si, sj = i, j

    # 스택 : 되돌아 갈 길 표시
    stack = [(1,1)]
    # visited : 방문한 곳 표시
    visited = [(1,1)]
    # 도착지점까지 갈 수 있으면 1, 없으면 0
    result = 0
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    while True:
        # 갈 수 있는 곳 찾기
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if arr[ni][nj] != '1' and (ni, nj) not in visited:
                si, sj = ni, nj
                stack.append((si, sj))
                visited.append((si, sj))
                break
        # 갈 수 있는 곳이 없을 때
        else:
            if stack:
                si, sj = stack.pop()
            else:
                break
        if arr[si][sj] == '3':
            result = 1
            break

    print('#{} {}' .format(tc, result))