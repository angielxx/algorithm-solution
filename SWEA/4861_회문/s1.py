# SWEA 4861_회문
# 220816

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    # 회문인 단어 넣을 리스트
    palindrome = list()
    # 행반복
    for i in range(N):
        # j : 비교하는 구간 맨 앞 인덱스
        for j in range(N - M + 1):
            strs = ''
            for k in range(M):
                strs += arr[i][j + k]

            palindrome.append(strs)
            strs = list(strs)
            while len(strs) > 1:
                if strs.pop(0) != strs.pop():
                    palindrome.pop()
                    break

    # 열반복
    for j in range(N):
        # j : 비교하는 구간 맨 앞 인덱스
        for i in range(N - M + 1):  # range(1)
            strs = ''
            for k in range(M):  # range(10) 0 ~ 9, i = 0
                strs += arr[i + k][j]  # 0 2

            # 임시로 저장해놓기
            palindrome.append(strs)

            strs = list(strs)
            while len(strs) > 1:
                # 대칭 아니면 임시로 저장해놓은거 삭제
                if strs.pop(0) != strs.pop():
                    palindrome.pop()
                    break

    print('#{}'.format(tc), *palindrome)