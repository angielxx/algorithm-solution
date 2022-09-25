
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 초기 설정
    pascal = [[1],[1, 1]]

    # 3번째 줄부터 생성
    for i in range(2, N):
        temp = [1] * (i+1)
        pascal.append(temp)
        # 1로 고정인 0번째 인덱스와 i번째 인덱스를 제외하고 값 계산
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print('#{}' .format(tc))
    for i in range(N):
        print(*pascal[i])