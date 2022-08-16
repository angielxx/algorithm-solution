# 4843_특별한_정렬
# 220811

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # N개의 정수를 받아 리스트에 저장
    arr = list(map(int, input().split()))

    # 길이가 N인 visit 리스트 생성
    # 정렬 리스트에 넣고 나면 해당 숫자의 인덱스의 False를 True로 바꾸기
    visit = [False] * N

    # 정렬해서 넣는 리스트
    new_arr = list()

    # 정렬 반복
    while len(new_arr) <= 10:
        # max, min 초기값
        max = 0
        min = 100
        # 인덱스 길이만큼 = 전체 리스트 순회하며 min, max 찾기
        for i in range(N):
            if visit[i] == False:
                if arr[i] >= max:
                    max = arr[i]
                if arr[i] <= min:
                    min = arr[i]
        # 새롭게 갱신한 min, max 정렬리스트에 넣고 visit는 True로
        if max == min:
            new_arr.append(max)
        else:
            new_arr.append(max)
            new_arr.append(min)

        visit[ arr.index(max) ] = True
        visit[ arr.index(min) ] = True
    
    print('#{}' .format(tc), *new_arr)