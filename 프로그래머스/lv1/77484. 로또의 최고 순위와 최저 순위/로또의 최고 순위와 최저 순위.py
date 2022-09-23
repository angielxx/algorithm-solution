def solution(lottos, win_nums):
    same_num = 0
    for i in lottos:
        for j in win_nums:
            if i == j:
                same_num += 1
    zero_cnt = 0
    for i in lottos:
        if i == 0:
            zero_cnt += 1
    min_num = same_num + 0
    max_num = same_num + zero_cnt
    # same_num : rank
    rank = { '6' : 1, '5' : 2, '4' : 3, '3' : 4, '2' : 5, '1' : 6, '0' : 6}
    answer = [ rank[f'{max_num}'], rank[f'{min_num}'] ]
    return answer