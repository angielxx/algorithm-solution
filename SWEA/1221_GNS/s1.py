# 1221_GNS
# 220812

"""
로직
1. 모든 단어를 하나의 리스트에 넣는다.
2. 단어 이름과 숫자를 쌍으로 딕셔너리에 저장해놓는다 (pairs)
3, 0부터 9의 쌍이 되는 문자열을 순서대로 넣을 딕셔너리를 만든다. key : val = 0~9 : []
3. num_list에서 문자열을 꺼내 pairs의 value와 같은 key를 가진 num_dict의 value안에 넣는다.
4. num_dict의 value인 모든 리스트를 순차적으로 출력한다.
"""

import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())

pairs = {
    "ZRO" : 0,
    "ONE" : 1,
    "TWO" : 2,
    "THR" : 3,
    "FOR" : 4,
    "FIV" : 5,
    "SIX" : 6,
    "SVN" : 7,
    "EGT" : 8,
    "NIN" : 9,
}

for _ in range(1, T+1):
    tc, N = input().split()
    N = int(N)

    # 모든 문자열을 저장
    num_list = list(input().split())

    # 정렬해서 넣을 딕셔너리, Key : Value = 번호 : []
    num_dict = { i : [] for i in range(10) }

    # 문자열 저장한 리스트 순회하며 pairs에서 문자열을 key로 value를 조회하여
    # num_dict의 맞는 key의 value에 넣어준다.
    for num in num_list:
        key = pairs[num]
        num_dict[key].append(num)

    # 최종 출력
    print('{}' .format(tc))
    # num_dict의 value인 리스트들만 꺼내서 출력한다.
    for key, val in num_dict.items():
        # 숫자 9에 대한 리스트일 때는 띄어쓰기를 하고
        if key == 9:
            print(*val)
        # 숫자 9가 아닐 때는 띄어쓰기를 하지 않는다.
        else:
            print(*val, end=' ')
