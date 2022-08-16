# SWEA 1216.회문2
# 220816
"""
100부터 줄여나가기
"""
import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    tc = int(input())

    # 문자열 그대로 1차원 리스트에 저장
    arr = [input() for _ in range(100)]

    # 90도 돌려서 미리 리스트 만들기
    arr2 = []
    for j in range(100):
        str = ''
        for i in range(100):
            str += arr[i][j]
        arr2.append(str)

    max = 0
    # 행 탐색
    length = 100
    status1 = False
    while status1 == False:
        # 모든 행
        for i in range(100):
            # 슬라이싱할 범위의 맨 앞 인덱스
            for j in range(100 - length + 1):
                slice = arr[i][j:j + length]
                if slice == slice[::-1]:
                    max = length
                    status1 = True
        else:
            length -= 1

    # 열 탐색 = arr2로 행 탐색 : 행으로 찾은 길이보다 긴 길이만 찾기
    length = max + 1
    status2 = False
    while length <= 100:
        # 모든 행
        for i in range(100):
            # 슬라이싱할 범위의 맨 앞 인덱스
            for j in range(100 - length + 1):
                slice = arr2[i][j:j + length]
                if slice == slice[::-1]:
                    max = length
        else:
            length += 1

    print('#{} {}' .format(tc, max))
