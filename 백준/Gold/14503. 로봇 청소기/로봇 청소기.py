import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split()) # 세로 i, 가로 j
si, sj, sd = map(int, input().split()) # 0, 1, 2, 3 북 동 남 서
room = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서 (시계방향)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j, d):
    dir = d
    cleaned = [[0] * m for _ in range(n)]
    answer = 0
    q = deque([(i, j)])
        
    def check(i, j):
        result = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= m or room[ni][nj] or cleaned[ni][nj]:
                continue
            result += 1
        return result

    while q:
        si, sj = q.popleft()
        
        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
        if not room[si][sj] and not cleaned[si][sj]:
            cleaned[si][sj] = 1
            answer += 1

        have = check(si, sj)
        # 청소되지 않은 빈칸이 있는 경우
        if have:
            for _ in range(4):
                dir -= 1
                if dir < 0: dir = 3
                ni = si + di[dir]
                nj = sj + dj[dir]
                if ni < 0 or ni >= n or nj < 0 or nj >= m or room[ni][nj] or cleaned[ni][nj]:
                    continue
                q.append((ni, nj))
                break
        # 청소되지 않은 빈칸이 없는 경우
        else:
            k = (dir + 2) % 4
            ni = si + di[k]
            nj = sj + dj[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            if room[ni][nj]:
                break
            q.append((ni, nj))
    return answer

answer = bfs(si, sj, sd)
print(answer)