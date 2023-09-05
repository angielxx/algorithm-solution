import sys
from collections import deque
input = sys.stdin.readline

# --- 입력 --- #

n = int(input()) # 지도 크기
k = int(input()) # 사과 개수

arr = [[0] * n for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split()) # 사과 위치
    arr[i-1][j-1] = 1

rotation = deque([])
l = int(input()) # 뱀의 방향 변환 횟수
for _ in range(l):
    a, b = input().split() # L, D
    rotation.append((int(a), b))

# --- 입력 --- #

# 북 동 남 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

dir = 1
snake = deque([(0,0)]) # 머리 - 몸통 - 꼬리

time = 0
while True:
    time += 1
    
    # 머리 위치
    hi, hj = snake[0]
    # 방향에 따른 다음 위치
    ni = hi + di[dir]
    nj = hj + dj[dir]
    
    # 벽 또는 자기자신의 몸과 부딪히는 경우
    if ni < 0 or ni >= n or nj < 0 or nj >= n or (ni, nj) in snake:
        break
    
    # 사과가 있다면
    if arr[ni][nj]:
        arr[ni][nj] = 0
    else:
        snake.pop() # 꼬리 빼기
    snake.appendleft((ni, nj)) # 머리 넣기
        
    # X초가 끝난 뒤 회전
    if rotation and rotation[0][0] == time:
        _, rotate = rotation.popleft()
        if rotate == 'L':
            dir -= 1
        else:
            dir += 1
        dir %= 4
        
print(time)