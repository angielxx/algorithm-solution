from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    limit = len(q1) * 4
    answer = 0
    while sum1 != sum2:
        
        if sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            q2.append(q1.popleft())
            answer += 1
        elif sum2 > sum1:
            sum2 -= q2[0]
            sum1 += q2[0]
            q1.append(q2.popleft())
            answer += 1
        else:
            break

        if answer == limit:
            answer = -1
            break
    return answer
            