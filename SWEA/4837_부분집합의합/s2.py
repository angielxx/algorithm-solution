# 4837_부분집합의 합
# 220811

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

# 집합 A 정의
A = [ a for a in range(1, 13)]
n = len(A)

for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 부분집합 검사
    # 원소의 개수와 합을 동시에 체크
    result = 0
    for i in range(1<<n):
        subset_cnt = subset_sum = 0
        for j in range(n):
            if i & (1<<j):
                subset_cnt += 1
                subset_sum += A[j]
        if subset_cnt == N and subset_sum == K:
            result += 1
    
    print('#{} {}' .format(tc, result))