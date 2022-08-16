# SWEA 5356. 의석이의 세로로 말해요
# 220816
"""
제일 긴 문자열 길이에 맞춰서 공백 붙이기
세로로 이어 붙이고 공백 삭제
"""
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = 5
    text_list = [ input() for _ in range(N)]

    # 제일 긴 문자열 구하기
    max_len = 0
    max_idx = 0
    for i in range(N):
        length = 0
        for s in text_list[i]:
            length += 1
        if length >= max_len:
            max_len = length
            max_idx = i

    # 제일 긴 문자열 길이만큼 공백 더하기
    for i in range(N):
        length = 0
        for s in text_list[i]:
            length += 1
        # 길이가 차이나는 만큼 공백 붙이기
        text_list[i] += ' ' * (max_len - length)

    # 세로로 이어 붙이기
    result = ''
    j = 0
    while j < max_len:
        i = 0
        while i < N:
            if text_list[i][j] == ' ':
                pass
            else:
                result += text_list[i][j]
            i += 1
        j += 1

    print('#{} {}' .format(tc, result))