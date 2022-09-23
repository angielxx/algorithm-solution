
import sys
input = sys.stdin.readline

# C가 세로
C, R = map(int, input().split())
# 내 좌석번호
K = int(input())

if K > R*C:
    print(0)
    exit()

# 좌석 배치도
arr = [[0] * R for _ in range(C)]

# 좌 > 하 > 우 > 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

dir = i = j = 0

for seat in range(1, R*C+1):
    if seat == K:
        print(i+1, j+1)
        break
    else:
        arr[i][j] = seat
        i += di[dir]
        j += dj[dir]

        # 유효성 검사
        if i < 0 or j < 0 or i >= C or j >= R or arr[i][j]:
            i -= di[dir]
            j -= dj[dir]
            dir = (dir + 1) % 4
            i += di[dir]
            j += dj[dir]