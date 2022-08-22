# BOJ 1904 01타일
# 220821

import sys
input = sys.stdin.readline

# 빙고판
arr1 = [list(map(int, input().split())) for _ in range(5)]
arr2 = [[0] * 5 for _ in range(5)]
arr3 = []
for _ in range(5):
    arr3 += list(map(int, input().split()))

def check_bingo(li):
    bingo = 0
    for i in range(5):
        if sum(li[i]) == 5:
            bingo += 1
    for j in range(5):
        row = []
        for i in range(5):
            row.append(li[i][j])
        if sum(row) == 5:
            bingo += 1
    x1 = [li[0][0], li[1][1], li[2][2], li[3][3], li[4][4]]
    if sum(x1) == 5:
        bingo += 1
    x2 = [li[4][0], li[3][1], li[2][2], li[1][3], li[0][4]]
    if sum(x2) == 5:
        bingo += 1
    return bingo

result = 0
status = False
for k in range(25):
    num = arr3[k]
    for i in range(5):
        for j in range(5):
            if arr1[i][j] == num:
                arr2[i][j] = 1
            if check_bingo(arr2) >= 3:
                result = k + 1
                status = True
                break
            else:
                pass
    if status:
        break
print(result)