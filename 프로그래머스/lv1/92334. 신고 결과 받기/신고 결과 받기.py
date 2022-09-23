import collections

def solution(id_list, report, k):
    # 메일 받은 횟수 저장
    mail = [0] * len(id_list)
    # 신고 당한 횟수 저장
    report_num = collections.defaultdict(int)
    # 신고한 경우를 모두 저장
    report_dict = collections.defaultdict(list)

    # 신고 내역 저장
    for i in range(len(report)):
        a, b = report[i].split()
        if b not in report_dict[a]:
            report_dict[a].append(b)
    
    for _, val in report_dict.items():
        for i in range(len(val)):
            report_num[val[i]] += 1

    for key, val in report_num.items():
        if val >= k:
            for person, li in report_dict.items():
                if key in li:
                    mail[id_list.index(person)] += 1

    return mail