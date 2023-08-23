import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

hi = [-1, -2, -2, -1, 1, 2, 2, 1]
hj = [-2, -1, 1, 2, -2, -1, 1, 2]

# visited[][][0] = 말 이동 사용 안하고 도착한 최소 이동수
# visited[][][k] = 말 이동 k번 사용하고 도착한 최소 이동수
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]

q = deque([(0, 0, 0, 0)]) # i, j, 말의 이동 사용한 횟수, 이동 횟수

flag = False
answer = 0
while q:
    i, j, num, dist = q.popleft()
    
    if i == h -1 and j == w - 1:
        answer = dist
        flag = True
        break
    
    # 말의 이동
    if num < k:
        for l in range(8):
            ni = i + hi[l]
            nj = j + hj[l]
            if ni < 0 or ni >= h or nj < 0 or nj >= w or arr[ni][nj]:
                continue
            if not visited[ni][nj][num + 1]:
                visited[ni][nj][num + 1] = 1
                q.append((ni, nj, num + 1, dist + 1))
    # 원숭이의 이동
    for l in range(4):
        ni = i + di[l]
        nj = j + dj[l]
        if ni < 0 or ni >= h or nj < 0 or nj >= w or arr[ni][nj]:
            continue
        if not visited[ni][nj][num]:
            visited[ni][nj][num] = 1
            q.append((ni, nj, num, dist + 1))
            
if not flag:
    print(-1)
else:
    print(answer)