def len(string):
    length = 0
    for s in string:
        length += 1
    return length

T = int(input())
for tc in range(1, T+1):
    N = 4
    arr = [list(input().split()) for _ in range(N)]

    # 상하좌우
    delta = [[-1,0], [1,0], [0,-1], [0,1]]
    # 만든 숫자 저장
    numbers = []
    def bfs(i, j, path=''):
        # i, j = 현재위치
        path += arr[i][j]
        if len(path) < 7:
            # 델타탐색으로 bfs
            for k in range(4):
                ni, nj = i+delta[k][0], j+delta[k][1]
                if 0 <= ni < N and 0 <= nj < N:
                    bfs(ni, nj, path)
        elif len(path) == 7:
            if path not in numbers:
                numbers.append(path)
    # 배열의 모든 위치에 대해 bfs
    for i in range(N):
        for j in range(N):
            bfs(i, j)
    print('#{}' .format(tc), len(numbers))