def solution(board, skill):
    answer = 0
    # 세로, 가로
    m = len(board)
    n = len(board[0])

    # 누적합 배열
    temp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        temp[r1][c1] += degree if type == 2 else -degree
        temp[r2+1][c1] -= degree if type == 2 else -degree
        temp[r1][c2+1] -= degree if type == 2 else -degree
        temp[r2+1][c2+1] += degree if type == 2 else -degree

    # 행 누적
    for i in range(m):
        for j in range(n):
            temp[i][j+1] += temp[i][j]

    # 열 누적
    for j in range(n):
        for i in range(m):
            temp[i+1][j] += temp[i][j]

    # 최종합
    for i in range(m):
        for j in range(n):
            board[i][j] += temp[i][j]
            if board[i][j] > 0: answer += 1

    return answer