# 2022 kakao blind recuitment
# programmers 주차 요금 계산
# 220920

import math

def solution(fees, records):
    # 주차 요금 정리
    basic_min = fees[0]
    basic_fee = fees[1]
    measure_min = fees[2] 
    measure_fee = fees[3]

    # 입출차내역 = "시각 차량번호 내역"
    # 시각 : HH:MM, 차량번호 : XXXX, 내역 : IN or OUT
    
    # total = 차량번호 : 총요금
    total = {}
    # memos = 차량번호 : [in, out]
    memos = {}
    for i in range(len(records)):
        time, carNum, move = records[i].split()
        if carNum not in memos.keys():
            memos[carNum] = []
        memos[carNum].append([move, time])
    print(memos)

    # 주차 시간 계산하는 함수
    def getTotalMin(time_in, time_out):
        H = int(time_out[0:2]) - int(time_in[0:2])
        M_in, M_out = int(time_in[3:]), int(time_out[3:])
        if M_in <= M_out:
            M = M_out - M_in
        # 12분, 10분
        else:
            M = (60 - M_in) + M_out
            H -= 1
        return H * 60 + M

    for carNum, memo in memos.items():
        # 최종 요금 저장할 딕셔너리 세팅
        if carNum not in total.keys():
            total[carNum] = 0
        
        time_in = time_out = 0
        total_min = 0
        for i in range(len(memo)):
            if memo[i][0] == "IN":
                time_in = memo[i][1]
                # in인데 마지막 내역일 때
                if i == len(memo) - 1:
                    time_out = '23:59'
                    total_min += getTotalMin(time_in, time_out)
            else:
                time_out = memo[i][1]
                total_min += getTotalMin(time_in, time_out)

        # 요금 계산
        # 기본 시간 이하 > 기본 요금 청구
        if total_min <= basic_min:
            total[carNum] = basic_fee
        # 기본 요금 초과 > 계산
        else:
            total[carNum] = basic_fee + math.ceil((total_min - basic_min) / measure_min) * measure_fee
    carNums = sorted(total.keys())
    result = []
    for carNum in carNums:
        result.append(total[carNum])
    return result







fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

solution(fees, records)