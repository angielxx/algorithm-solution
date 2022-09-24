# SWEA 1953 탈주범 검거
# 220913


T = int(input())

def length(iterable):
    l = 0
    for i in iterable:
        l += 1
    return l

# 델타탐색 : 상하좌우
delta = [[-1,0],[1,0],[0,-1],[0,1]]
# key = 터널 구조물 타입, value = 갈 수 있는 방향(상하좌우, 0 1 2 3)
way = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2],
}

# 방향 바꾸기
def convert(dir):
    if dir == 0:
        dir = 1
    elif dir == 1:
        dir = 0
    elif dir == 2:
        dir = 3
    elif dir == 3:
        dir = 2
    return dir

for tc in range(1,T+1):
    # 세로, 가로, 맨홀 세로, 맨홀 가로, 탈출 후 소요된 시간
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []

    cnt = 0
    def bfs(R, C):
        global cnt

        queue = [(R, C)]
        hour = 0
        while queue:
            hour += 1
            if hour <= L:
                for _ in range(length(queue)):
                    si, sj = queue.pop(0)
                    visited.append((si, sj))
                    cnt += 1

                    # 터널 타입에 따라 델타 탐색하여 연결 확인
                    type = arr[si][sj]
                    for k in way[type]:
                        ni, nj = si + delta[k][0], sj + delta[k][1]
                        # 유효성 확인, 방문했는지 확인
                        if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited:
                            # 터널이 있는지, 연결되어 있는지 확인
                            if arr[ni][nj] != 0 and convert(k) in way[arr[ni][nj]] and (ni, nj) not in queue:
                                queue.append((ni, nj))
            else:
                break

    # bfs 시작
    bfs(R, C)
    print('#{}' .format(tc), cnt)
