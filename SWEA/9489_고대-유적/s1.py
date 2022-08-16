# 9489_고대-유적
# 220812

# 런타임 에러!

import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())

# 매개변수 : 배열, 가로, 세로
def get_cnt(arr, N, M): 
    global max
    for i in range(N):
        # 한 행에 대해 카운트
        cnt = 0
        for j in range(M):
            # 1이면 자기자신을 세고 뒤에 원소가 더 있는지 (본인이 마지막인지 아닌지) 확인
            if arr[i][j] == 1:
                cnt += 1
                # j가 마지막 열이라면 -> 자기자신만 세고 cnt 비교 cnt 초기화
                if j == M - 1:
                    # print(i, cnt)
                    if cnt >= max:
                        max = cnt
                    # 최댓값이 아니더라도 초기화해야하니까 if문 밖으로 꺼내준다.
                    cnt = 0
                # j가 마지막 열이 아니라면-> 다음을 보러 넘어간다
                else:
                    pass
            # 0이면 cnt 비교하고 cnt 초기화
            else:
                if cnt >= max:
                    max = cnt
                cnt = 0


for tc in range(1, T+1):
    # N : 행의 개수, M : 열의 개수
    N, M = map(int, input().split())

    # 2차원 배열 생성
    arr = [ list(map(int, input().split())) for _ in range(N)]

    # arr 90도 돌려놓기
    arr_rotate = [ [0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            arr_rotate[i][j] = arr[N-j-1][i]

    # 최댓값 저장할 변수
    max = 0

    # 가로축으로 탐색
    get_cnt(arr, N, M)

    # 세로축으로 탐색 (90도로 회전시킨 배열을 넣어준다.)
    get_cnt(arr_rotate, M, N)

    print('#{} {}' .format(tc, max))