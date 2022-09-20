# SWEA 4366 정식이의 은행업무
# 220920

import sys
sys.stdin = open('sample_input.txt', 'r')

def len(string):
    length = 0
    for s in string:
        length += 1
    return length

T = int(input())
for tc in range(1, T+1):
    # 2진수
    A = list(input())
    # 3진수
    B = list(input())

    # A,B 각 인덱스번째의 숫자를 바꿨을 때 나오는 숫자를 set에 저장
    A_case = []
    B_case = []

    # 이진수
    for i in range(len(A)):
        temp = A[::]
        if A[i] == '0':
            temp[i] = '1'
        else:
            temp[i] = '0'
        binary = ''.join(temp)
        A_case.append(int('0b'+binary, 2))
    
    # 3진수를 10진수로
    def triToDec(tri):
        dec = 0
        for i in range(len(tri)):
            dec += (3**i) * int(tri[i])
        return dec

    #3진수
    for i in range(len(B)):
        for num in ['0', '1', '2']:
            temp = B[::]
            temp[i] = num
            B_case.append(triToDec(temp))
    result = set(A_case) & set(B_case)
    print('#{}' .format(tc), *result)
            