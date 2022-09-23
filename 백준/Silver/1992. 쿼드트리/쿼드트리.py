import sys
input = sys.stdin.readline

N = int(input())
arr = [ input() for _ in range(N)]

def quadTree(i_start=0, i_end=N-1, j_start=0, j_end=N-1):
    num = arr[i_start][j_start]
    status = True
    for i in range(i_start, i_end+1):
        if not status:
            break
        for j in range(j_start, j_end+1):
            if arr[i][j] != num:
                status = False
                break
    if status:
        return num
    else:
        i_mid = (i_start + i_end) // 2
        j_mid = (j_start + j_end) // 2
        return '({}{}{}{})' .format(quadTree(i_start, i_mid, j_start, j_mid), quadTree(i_start, i_mid, j_mid+1, j_end), quadTree(i_mid+1, i_end, j_start, j_mid), quadTree(i_mid+1, i_end, j_mid+1, j_end))

print(quadTree())