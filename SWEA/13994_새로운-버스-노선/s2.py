# 13994_새로운-버스-노선
# 220813

# 런타임에러!

from sre_constants import MIN_REPEAT
import sys
sys.stdin = open('sample_in.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 노선수
    N = int(input())

    bus_dict = dict()
    # 노선 정보 저장
    min_A = 100
    max_B = 0
    for _ in range(N):
        num, A, B = map(int, input().split())
        bus_dict[num] = (A, B)
        if max_B <= B:
            max_B = B

    route = [0] * max_B

    for key, val in bus_dict.items():
        num = key
        A, B = val
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