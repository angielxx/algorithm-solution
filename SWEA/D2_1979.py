"""idea
count = 0
1일때 count += 1 이다가
0을 만나면 count 저장하고 count = 0 초기화
테스트 케이스마다 정답은 count의 요소 중 K와 같은 것의 갯수
"""

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split(' '))
    puzzle = []

    for i in range(N):
        puzzle.append(list(map(int, input().split())))

    result = []

    #행 검사
    for i in range(N):  #행 번호
        count = 0
        for j in range(N):  # 길이만큼 각 원소 반복해서
            if puzzle[i][j] == 1:
                count += 1
            else:
                result.append(count)
                count = 0 
        result.append(count)

    """
    오답 : puzzle_rotate = puzzle"""
    new = [[0] * N for _ in range(N)]

    #90도 돌린 퍼즐 생성
    for i in range(N): # 0~4
        for j in range(N):
             new[j][N - i -1] = puzzle[i][j]

    #돌린 퍼즐로 검사
    for i in range(N):
        count = 0
        for j in range(N):
            if new[i][j] == 1:
                count += 1
            else:
                result.append(count)
                count = 0 
        result.append(count)
    
    count_number = result.count(K)
    print(f'#{t} {count_number}')