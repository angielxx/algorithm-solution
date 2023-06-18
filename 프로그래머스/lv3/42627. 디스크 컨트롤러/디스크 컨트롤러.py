# 우선순위큐 사용
# 하드 디스크가 쉬면 안됨
# 현재 시점에서 작업할 수 있는 태스크가 있으면 다음 순서로 넣는다.
# 아무것도 없다면 현재 시점을 늘린다.
# 우선순위큐 

import heapq
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)