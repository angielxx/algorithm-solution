# 2022 kakao blind recuitment
# programmers k진수에서 소수 구하기
# 220920

import math

# 소수 판별 함수
def is_prime(x):
    x = int(x, 2)
    print(x)
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    else:
        return True

# 문제 조건에 맞는 소수인지 판별하는 함수
def is_ok(base, num, s, e):
    front = s-1
    back = e+1
    status = False
    if 0 <= front < len(base):
        if base[front] == '0':
            # case1 
            if 0 <= back < len(base) and base[back] == '0':
                status = True
            # case3
            if back >= len(base):
                status = True
    # case2
    if 0 <= back < len(base) and base[back] == '0' and front < 0:
        status = True
    if front < 0 and back >= len(base):
        status = True
    return status

def solution(n, k):

    # 작은 수 부터 넣는다
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    number = rev_base[::-1]

    cnt = 0
    for s in range(len(number) - 1):
        for e in range(s, len(number)):
            part = number[s:e+1]
            if '0' not in part and part != '1' and is_prime(int(part)):
                if is_ok(number, part, s, e):
                    cnt += 1
    return cnt

n = 437674
k = 3
# n = 110011
# k = 10

print(solution(n, k))