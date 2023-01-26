from collections import deque

def solution(numbers, target):
    cnt = 0

    # (depth, total)
    Q = deque([(0, numbers[0]), (0, (-1) * numbers[0])])
    
    while Q:
        depth, total = Q.popleft()
        if depth + 1 < len(numbers):
            Q.append((depth + 1, total + numbers[depth + 1]))
            Q.append((depth + 1, total - numbers[depth + 1]))
        else:
            if total == target: cnt += 1

    return cnt