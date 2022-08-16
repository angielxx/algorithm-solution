# 13994_새로운-버스-노선
# 220813

# 런타임에러!

import sys
sys.stdin = open('sample_in.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 노선수
    N = int(input())

    # 1 <= N <= 100
    # 인덱스 0부터 100까지 있어야하므로 *101
    route = [0] * 101 

    # 노선 정보 저장
    for _ in range(N):
        num, A, B = map(int, input().split())
        # 일반버스
        if num == 1:
            for i in range(A, B + 1):
                route[i] += 1
        # 급행버스
        elif num == 2:
            # A가 홀수
            if A % 2:
                # A ~ B 중 홀수에만 +1
                for i in range(A, B+1):
                    if i % 2:
                        route[i] += 1
            # A가 짝수
            else:
                # A ~ B 중 짝수에만 +1
                for i in range(A, B+1):
                    if i % 2 == 0:
                        route[i] += 1
        # 광역급행 버스
        elif num == 3:
            # A가 홀수
            if A % 2:
                for i in range(A, B+1):
                    if i % 3 == 0 and i % 10 != 0:
                        route[i] += 1
            # A가 짝수
            else:
                for i in range(A, B+1):
                    if i % 4 == 0:
                        route[i] += 1
    # 가장 큰 숫자를 가진 정류장 찾기
    max = 0
    for i in range(len(route)):
        if route[i] >= max:
            max = route[i]
    
    print('#{} {}' .format(tc, max))
