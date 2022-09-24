T = int(input())

# 좌상부터 시계방향 0 ~ 7 에 따라 행, 열의 값 변화
dir = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

# T, X 방향으로 바꿀 수 있는 돌이 있는지 확인하는 함수
# si, sj : 현재 놓은 돌의 위치, color : 나의 색깔
def change(sj, si, color):
    global arr

    enemy = 'W' if color == 1 else 'B'
    me = 'B' if color == 1 else 'W'

    for k in range(8):
        # 방향 k에 대해 계속 상대 돌이 나오는지 확인
        i = 1
        status = False
        stack = []
        while True:
            ni, nj = si + dir[k][0] * i, sj + dir[k][1] * i
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == enemy:
                stack.append((ni, nj))
                i += 1
            # 연속해서 enemy 나오다가 자기자신이면
            elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == me:
                status = True
                break
            # 0이 나와도 중단
            else:
                break
        # print(stack, k, status)
        while stack and status:
            ki, kj = stack.pop()
            arr[ki][kj] = me
            # print('change', arr)

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]

    # 초기 흑돌 백돌 배치
    arr[N//2 - 1][N//2 - 1] = 'W'
    arr[N//2][N//2] = 'W'
    arr[N//2 - 1][N//2] = 'B'
    arr[N//2][N//2 - 1] = 'B'

    # (j, i, 1:흑돌 / 2:백돌)
    for _ in range(M):
        j, i, color = map(int, input().split())
        # 번호를 -1하여 인덱스로 변환
        j, i = j-1, i-1
        arr[i][j] = 'B' if color == 1 else 'W'
        # print(arr)
        change(j, i, color)
    # 개수 세기
    W_cnt = B_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'W':
                W_cnt += 1
            elif arr[i][j] == 'B':
                B_cnt += 1
    print('#{}' .format(tc), B_cnt, W_cnt)