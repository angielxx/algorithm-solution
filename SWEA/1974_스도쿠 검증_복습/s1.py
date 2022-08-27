# SWEA 스도쿠검증 복습
# 220827

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

nums = [1,2,3,4,5,6,7,8,9]

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    status = True
    # 행 탐색
    for i in range(9):
        row = sudoku[i]
        row = list(set(row))
        if row != nums:
            status = False
            break
    # 열 탐색
    if status:
        for j in range(9):
            col = []
            for i in range(9):
                col.append(sudoku[i][j])
            col = list(set(col))
            if col != nums:
                status = False
                break

    # 3*3 박스 탐색
    if status:
        for i in [0,3,6]:
            for j in [0,3,6]:
                if status:
                    box = []
                    for k in range(3):
                        for l in range(3):
                            box.append(sudoku[i+k][j+l])
                    box = list(set(box))
                    if box != nums:
                        status = False
                        break
    if status:
        result = 1
    else:
        result = 0
    print('#{} {}'.format(tc, result))