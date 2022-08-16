# 4839_이진탐색
# 220811

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def get_cnt(l, r, cnt, P): # A_cnt, B_cnt 받는다.
    cnt += 1
    # C계산
    C = int((l + r) / 2)
    
    # P 찾았는지 확인
    if C == P:
        # 찾았으면 cnt 반환
        return cnt
    else:
        # 못 찾았으면 재귀호출로 다음 탐색 시작
        if C < P:
            l = C
        else:
            r = C
        return get_cnt(l, r, cnt, P) # return 없이 그냥 재귀호출만 하니까 None됨
        

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    # 처음 l, r은 동일
    la, ra = 1, P
    lb, rb = 1, P

    # 카운트 0으로 초기 설정
    A_cnt = B_cnt = 0

    A_cnt = get_cnt(la, ra, A_cnt, Pa)
    B_cnt = get_cnt(lb, rb, B_cnt, Pb)

    # A와 B의 탐색 횟수 비교하고 승부 가리기
    if A_cnt == B_cnt:
        result = 0
    else:
        result = 'A' if A_cnt < B_cnt else 'B'
    
    print('#{} {}' .format(tc, result))