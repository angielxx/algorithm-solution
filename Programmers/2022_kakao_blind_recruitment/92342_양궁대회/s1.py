# 2022 kakao blind recuitment
# programmers 양궁대회
# 220920

import copy

def solution(n, info):
    # 어피치 현재 점수 계산
    apeach = 0
    # 라이언 경우의 수 모두 저장
    ryan = []
    i = 0
    temp = copy.deepcopy(info)
    while temp:
        num = temp.pop(0)
        if num:
            apeach += i
        i += 1

    max_diff = 0
    max_list = []
    # s는 스타트 지점
    for s in range(len(info)):
        i = s
        N = n
        case = [0] * 11
        while N:
            if info[i] < N: 
                case[i] = info[i] + 1
                N -= case[i]
            i += 1
        print(case)
        # 점수 비교하기
        # print(info)
        # print(case)
        apeach_score, ryan_score = 0, 0
        for i in range(len(info)):
            score = len(info) - i - 1
            if info[i] > case[i]:
                apeach_score += score
            elif info[i] < case[i]:
                ryan_score += score
            elif info[i] == case[i] and info[i] != 0:
                apeach_score += score

        # 라이언이 더 높은 점수라면
        if apeach_score < ryan_score:
            diff = ryan_score - apeach_score
            if diff > max_diff:
                max_list = [case]
                max_diff = diff
            elif diff == max_diff:
                max_list.append(case)
    print(max_list)
    result = 0
    if not max_list:
        result = [-1]
        
    answer = []
    return answer


# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]
# n = 1
# info = [1,0,0,0,0,0,0,0,0,0,0]
# n = 9
# info = [0,0,1,2,0,1,1,1,1,1,1]
n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
solution(n, info)
