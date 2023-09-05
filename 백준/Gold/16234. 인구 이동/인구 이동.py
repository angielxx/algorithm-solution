import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split()) # 땅 크기 / 인구차이 l명 이상, r명 이하
arr = [list(map(int, input().split())) for _ in range(n)]


di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

time = 0
while True:
    visited = [[0] * n for _ in range(n)]
    union_cnt = 0
    
    # for a in arr:
    #     print(a)
    # print()

    def bfs_union(i, j):
        global union_cnt
        
        q = deque([(i, j)])
        visited[i][j] = 1
        union = [(i, j)]
        
        total = arr[i][j]
        cnt = 1 # 한 연합안의 나라 갯수
        
        while q:
            si, sj = q.popleft()
            
            for k in range(4):
                ni = si + di[k]
                nj = sj + dj[k]
                
                if ni<0 or ni>=n or nj<0 or nj>=n or visited[ni][nj]:
                    continue
                
                diff = abs(arr[ni][nj] - arr[si][sj])
                if l <= diff <= r: # 인구차이가 l명 이상, r명 이하라면
                    q.append((ni, nj))
                    union.append((ni, nj))
                    visited[ni][nj] = 1
                    
                    cnt += 1
                    total += arr[ni][nj]
        if cnt == 1:
            return
        population = total // cnt

        for i, j in union:
            arr[i][j] = population
            
        union_cnt += 1
        return 
        
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs_union(i, j)
    if not union_cnt:
        break
    
    time += 1
    
print(time)