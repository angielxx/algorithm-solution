# 4837_부분집합의 합
# 220811

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

# 집합 A 정의
A = [ a for a in range(1, 13)]
n = len(A)

# 부분집합 반복문 전에 만들기 (시간복잡도 줄이기)
subset_list = []
for i in range(1<<n):
    subset_i = []
    for j in range(n):  # 오답! range(1, 13)으로 함 -> j는 원소들의 인덱스값이다!
        if i & (1<<j):
            subset_i.append(A[j])
    subset_list.append(subset_i)

for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 조건에 부합하는 부분집합 카운트
    cnt = 0
    for subset in subset_list:
        # 길이가 N이면 합을 구하는 연산을 시작한다.
        if len(subset) == N:
            sum = 0
            for num in subset:
                sum += num
            if sum == K:
                cnt += 1

    print('#{} {}' .format(tc, cnt))
