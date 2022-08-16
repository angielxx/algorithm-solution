# 1213_String
# 220812

import sys
sys.stdin = open('test_input.txt', 'r', encoding='utf-8')

T = 10

for _ in range(1, T+1):
    tc = input()
    goal = input()
    sentence = input()

    # 목표값의 길이만큼 슬라이싱하여 goal과 비교
    length = len(goal)

    cnt = 0
    # i는 0부터 N - length
    for i in range(len(sentence) - length): 
        if sentence[i : i + length] == goal:
            cnt += 1
    
    print('#{} {}' .format(tc, cnt))