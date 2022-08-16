# SWEA 4831 전기버스
# 220809

import sys

sys.stdin = open('sample_input.txt' , 'r')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    # 정류장들 리스트
    stops = [0] * N

    # 충전소 리스트
    idx_list = list(map(int, input().split()))

    # 정류장들 상태 변경 (충전기 있으면 1)
    for idx in idx_list:
        stops[idx] = 1

    # 현재 위치, 충전 횟수 0으로 초기화
    current_idx = 0
    cnt = 0
    # 최종출력할 값인 result는 0으로 초기화, 종점까지 간 경우에 cnt값으로 재할당
    result = 0

    # True로 일단 무조건 K만큼 이동은 하기로 한다.
    while True:
        current_idx += K
        # 이동 후 종점이 아니라면 충전기 설치여부 확인
        if current_idx < N:
            # 충전기가 있을 경우
            if stops[current_idx] == 1:
                cnt += 1
            # 충전기가 없을 경우
            else:
                # 지나온 정류장 중에 충전기가 있는 정류장을 탐색하고 뒤로 이동
                for find_idx in range(current_idx, current_idx - K, -1):
                    if stops[find_idx] == 1:
                        current_idx = find_idx
                        cnt += 1
                        # 찾았으면 for문 중단!
                        break
                    else:
                        pass
                # 충전기가 있는 정류장 못 찾으면 result는 그대로 0, while문 중단!
                else:
                    result = 0
                    break
        # 이동 후 종점이라면 result를 cnt로 재할당하고, while문 중단!
        else:
            result = cnt
            break

    print('#{} {}' .format(tc, result))
    
        
