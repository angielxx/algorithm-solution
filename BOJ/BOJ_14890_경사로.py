# BOJ 14890 경사로
# 220826

"""
일단 경사로를 지을 수 있으면(경사로 길이보다 길기만하면) 경사로를 짓는다.
경사로는 겹칠 수 없으므로 모두 1이어야한다.
경사로를 모두 지은 후, 경사로를 검사하여 경사로 중에 2이상이면 제외한다.
"""

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
# 한개의 행 또는 열을 넣어서 검사하는 함수
def check_slope(row):
    global slope_cnt

    # 지나갈 수 없는 길이라면 False
    status = True
    for j in range(N-1):
        # 숫자가 커지는 경우
        if row[j] + 1 == row[j+1]:
            # 나 자신도 연속하는 1작은 수이므로 1부터 시작
            cnt = 1
            k = 1
            # 내려가면서 세기
            while 0 <= j - k:
                # 연속하거나 경사로가 지어져있지 않다면 센다
                if row[j-k] == row[j] and slope[j-k] == 0:
                    cnt += 1
                    k += 1
                else:
                    break
            # 연속된 숫자가 L보다 작으면 경사로를 지을 수 없다.
            if cnt < L:
                status = False
                break
            # 경사로를 지을 수 있다면 경사로 짓기
            if status:
                for k in range(L):
                    if slope[i][j-k] == 0:
                        slope[i][j-k] = 1
        # 숫자가 1 작아진다면 그 숫자 개수 세기
        if row[j] - 1 == row[j+1]:
            # 나 자신은 연속하는 수에 포함되지 않으므로 0부터 시작
            cnt = 0
            k = 1
            # 올라가면서 세기
            print('check',slope)
            while j + k < N:
                if row[j+k] == row[j] - 1 and slope[j+k] == 0:
                    cnt += 1
                    k += 1
                else:
                    break
            if cnt < L:
                status = False
                break
            if status:
                for k in range(1, L+1):
                    slope[i][j+k] = 1
    print(row)
    print(status)
    if status:
        slope_cnt += 1

slope_cnt = 0
# 경사로
slope = [[0]*N for _ in range(N)]
# 행 탐색
# for i in range(N):
#     check_slope(arr[i])
# 경사로
slope = [[0]*N for _ in range(N)]
# 열 탐색
for j in range(N):
    col = []
    for i in range(N):
        col.append(arr[i][j])
    check_slope(col)
print(slope_cnt)