# SWEA 1208 Flatten
# 220809

import sys

sys.stdin = open('input.txt' , 'r')

for tc in range(1, 10+1):
    dump = int(input())

    # 기둥들 저장
    cols = list(map(int, input().split()))

    # 최대 최소 기둥 찾기
    while True:
        max, min = 1, 100
        max_idx = min_idx = 0

        for idx in range(100):
            if cols[idx] >= max:
                max = cols[idx]
                max_idx = idx
            else:
                pass
            if cols[idx] <= min:
                min = cols[idx]
                min_idx = idx
            else:
                pass
        
        # dump가 남아있으면 상자 옮기기
        if dump > 0:
            cols[max_idx] = max - 1
            cols[min_idx] = min + 1
            dump -= 1
        # 없으면 min, max 찾기 끝
        else:
            break

    # 최대점, 최저점의 차
    result = max - min
    print('#{} {}' .format(tc, result))