# 연습문제2_정수를-문자열로-변환
# 220812

import sys
sys.stdin = open('input.txt', 'r')

def itoa(n):
    if n == 0:
        return '0'
    if n > 0:
        flag = True
    else:
        n = -(n)
        flag = False
    
    # 최종 문자열
    result = ''

    while n:
        # 1의 자리수를 제외한 앞의 숫자들
        remain = n % 10
        # 1의 자리수
        n = n // 10
        
        result = chr(ord('0') + remain) + result
    # result = result[::-1]
    
    if flag:
        return result
    else:
        return '-' + result

for i in range(1, 7):
    tc = i
    num = int(input())
    result = itoa(num)
    
    print('#{} {}' .format(tc, result), end=" <class 'str'>\n")

