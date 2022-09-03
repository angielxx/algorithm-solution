# 200. Number of Islands
# 220901

# PASS

"""
로직
1. n*m 순회
2. 1이라면 델타탐색 시작
3. 1이면 visited를 1로 바꾸고 해당 위치로 이동
4. 델타탐색 중에 방문하지 않은 곳이면서 1인 곳이 없을 때까지 반복

상하좌우 중 먼저 한 곳에 가버리고 나면 나머지 1인 애들을 다시 방문해야함
> stack에 넣어놔야함
"""

class Solution(object):
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])

        delta = [[-1,0], [1,0], [0,-1], [0,1]]
        visited = [[False]*m for _ in range(n)]

        # 섬의 개수
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and visited[i][j] == False:
                    cnt += 1
                    # 현재 위치
                    si, sj = i, j
                    visited[si][sj] = True
                    stack = [(si, sj)]
                    # 델타 탐색 반복
                    while stack:
                        # print(stack)
                        # 스택에서 꺼내 위치 이동
                        si, sj = stack.pop()
                        # print(si, sj)
                        visited[si][sj] = True
                        # 델타의 1인 모든 위치 스택에 저장해놓기
                        for k in range(4):
                            ni, nj = si + delta[k][0], sj + delta[k][1]
                            # 유효성 검사
                            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '1' and visited[ni][nj] == False:
                                stack.append((ni, nj))
                            else:
                                pass
                # '0'이면 넘어감
                else:
                    pass
        return cnt   

        
        
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# grid = [
#     ["1","1","1"],
#     ["0","1","0"],
#     ["0","1","0"]]

s = Solution()
print(s.numIslands(grid))