# BOJ 1946 신입사원
# 220830
# 풀이 참고 여부 : yes

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    score.sort()

    cnt = 1
    # 1등의 사람의 면접 순위
    top = score[0][1]
    for i in range(1, N):
        if score[i][1] < top:
            cnt += 1
            top = score[i][1]
        else:
            pass
    print(cnt)