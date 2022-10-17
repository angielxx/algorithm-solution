# BOJ 2630 색종이만들기
# 221017

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def checkPaper(si, ei, sj, ej):
    color = arr[si][sj]

    flag = True
    for i in range(si, ei + 1):
        for j in range(sj, ej + 1):
            if arr[i][j] != color:
                flag = False
    if flag:
        if color == 1:
            return 'blue'
        else:
            return 'white'
    else:
        return False

white = blue = 0
def split(si, ei, sj, ej):
    global white
    global blue

    if checkPaper(si, ei, sj, ej) == 'blue':
        blue += 1
        return
    elif checkPaper(si, ei, sj, ej) == 'white':
        white += 1
        return

    mid_i = (si + ei) // 2
    mid_j = (sj + ej) // 2
    split(si, mid_i, sj, mid_j)
    split(mid_i + 1, ei, sj, mid_j)
    split(si, mid_i, mid_j + 1, ej)
    split(mid_i + 1, ei, mid_j + 1, ej)

    
split(0, N-1, 0, N-1)
print(white)
print(blue)