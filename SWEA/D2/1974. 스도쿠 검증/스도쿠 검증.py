
T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    number = {1,2,3,4,5,6,7,8,9}
    # 결과 1로 두고, 하나라도 조건에 안 맞으면 0
    result = 1
    # while로 두고 하나라도 조건에 안 맞으면 break

    i = 0
    # 행검증
    while i < 9:
        row = set(arr[i])
        if row == number:
            i += 1
        else:
            result = 0
            break
    # 열 검증
    if result == 1:
        for j in range(9):
            col = []
            for i in range(9):
                col.append(arr[i][j])
            col = set(col)
            if col == number:
                i += 1
            else:
                result = 0
                break
    # 정사각 검증
    if result == 1:
        # 어차피 모든 테케에서 고정이니까 반복문 쓰지 않고 만들어놓기
        position = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

        # 정사각 안의 행, 열 증가값
        di = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        dj = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        for pos in position:
            # 정사각 안의 모든 원소를 저장할 리스트
            sqr = []
            # 기준이 되는 원점
            ni, nj = pos
            for k in range(9):
                i = ni + di[k]
                j = nj + dj[k]
                sqr.append(arr[i][j])
            sqr = set(sqr)
            if sqr == number:
                pass
            else:
                result = 0
                break

    print('#{} {}' .format(tc, result))