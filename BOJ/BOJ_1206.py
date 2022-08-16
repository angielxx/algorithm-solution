# 1206_view
# 220808

for tc in range(1, 10+1):
    T = int(input())

    # 2차원 배열 만들기 (90도 회전시켜서)
    arr = list()
    for _ in range(T):
        arr.append([0] * 255)

    # 기둥 저장
    cols = list(map(int, input().split()))

    # arr를 기둥길이에 맞게 1로 변경
    for i in range(T): # 세로
        col = cols[i]
        for j in range(col): # 가로
            arr[i][j] = 1
    
    # cnt 초기화
    cnt = 0
    # 1이면 위, 아래 조건 확인
    for i in range(T):
        for j in range(255):
            if arr[i][j] == 1:
                if arr[i+1][j] == 0 and arr[i+2][j] == 0 and arr[i-1][j] == 0 and arr[i-2][j] == 0:
                    cnt += 1
                else:
                    pass
            else:
                pass
    print('#{} {}' .format(tc, cnt))