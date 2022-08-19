# BOJ 2559 수열
# 220819

N, L = map(int, input().split())

# 원본 배열
arr = [list(map(int, input().split())) for _ in range(N)]

# 숫자 하락
# 범위 유효성 확인
# 경사로 있는지 확인
# 경사로 짓기

def check_row(row):
    # 한 행에 대한 경사로 체크
    slope = [0] * N
    # 한 줄에 대한 상태
    status = True

    # 정방향으로
    for j in range(N-1):
        if row[j] != row[j+1] + 1:
            if row[j] == row[j+1] + 1:
                num = row[j+1]
                # 범위 유효성 확인
                if j + L > N - 1:
                    status = False
                    break
                # 연속 숫자 확인
                for k in range(1, L+1):
                    if row[j+k] != row[j+1]:
                        status = False
                        break
                # 연속이 확인됨!
                else:
                    for k in range(1, L+1):
                        slope[j+k] += 1
            else:
                status = False
    # 역방향으로
    row = row[::-1]
    slope = slope[::-1]
    for j in range(N - 1):
        if row[j] != row[j + 1] + 1:
            if row[j] == row[j + 1] + 1:
                num = row[j + 1]
                # 범위 유효성 확인
                if j + L > N - 1:
                    status = False
                    break
                # 연속 숫자 확인
                for k in range(1, L + 1):
                    if row[j + k] != row[j + 1]:
                        status = False
                        break
                # 연속이 확인됨!
                else:
                    for k in range(1, L + 1):
                        slope[j + k] += 1
            else:
                status = False
    slope = slope[::-1]
    print(i, slope, status)
    return status

# 행탐색
for i in range(N):
    row = arr[i]

    # 각 행 개별로 검사
    check_row(row)






# # 열탐색
# for j in range(N):
#     col = []
