from collections import deque

def solution(maps):
    # i, j
    n, m = len(maps), len(maps[0])
    # 최댓값
    answer = n * m
    flag = False
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    # 거리 계산 + 방문처리
    graph = [[-1 for _ in range(m)] for _ in range(n)]
    
    # [(i, j)]
    Q = deque([(0, 0)])
    while Q:
        si, sj = Q.popleft()
        
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] == 1:
                maps[ni][nj] = maps[si][sj] + 1
                Q.append((ni, nj))
    print(maps)
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]