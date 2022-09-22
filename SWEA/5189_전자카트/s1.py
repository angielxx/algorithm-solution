# SWEA 5188 최소합
# 220922

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_battery = N*N*100
    def switch(i, case):
        global min_battery

        # 종료, 비교 조건
        if i == N-1:
            print(case)
            battery = 0
            for j in range(N):
                s, e = case[j], case[j+1]
                # print(s,e)
                battery += arr[s-1][e-1]
            if battery < min_battery:
                min_battery = battery
            return

        path = case[:]
        # print(path)
        for j in range(i, N):
            path[i], path[i+1] = path[i+1], path[i]
            switch(j+1, path)
            path[i], path[i+1] = path[i+1], path[i]

    # 시작
    case = [ i for i in range(1, N+1)] + [1]
    for i in range(1, N):
        switch(i, case)

    print('#{}' .format(tc), min_battery)