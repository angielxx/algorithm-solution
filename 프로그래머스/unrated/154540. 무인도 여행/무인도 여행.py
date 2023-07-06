from collections import deque

def solution(maps):
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))];
    
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    answer = []
    
    def bfs(ai, aj):
        nonlocal answer
        nonlocal visited
        
        q = deque([[ai, aj]])
        visited[ai][aj] = 1
        total = int(maps[ai][aj])

        while q:
            si, sj = q.popleft()

            for i in range(4):
                ni = si + di[i]
                nj = sj + dj[i]
                
                if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]) and maps[ni][nj] != 'X' and visited[ni][nj] == 0:
                    q.append([ni, nj])
                    total += int(maps[ni][nj])
                    visited[ni][nj] = 1
                    visited
        answer.append(total)
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                bfs(i, j)
                
    if (not answer): return [-1]
    return sorted(answer)