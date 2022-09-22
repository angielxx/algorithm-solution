# SWEA 5188 최소합
# 220922

# 집합 dfs로 풀기

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1 2 3 1 > 가운데 2 3 인 길
    case = [i for i in range(2, N+1)]

    min_battery = N*N*100
    def dfs(path):
        global min_battery

        # 종료 조건
        if len(path) == N-1:
            # print(path)
            path = [1] + path + [1]
            battery = 0
            for i in range(N):
                s, e = path[i], path[i+1]
                battery += arr[s-1][e-1]
            if battery < min_battery:
                min_battery = battery
            return

        for i in range(2, N+1):
            if i not in path:
                dfs(path + [i])

    for i in range(2, N+1):
        dfs([i])
    print('#{}' .format(tc), min_battery)