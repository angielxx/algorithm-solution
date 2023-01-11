def solution(s):
    from collections import deque
    import copy
    arr = list(s)
    arr = deque(arr)

    pair = {
        ')':'(',
        ']':'[',
        '}':'{',
    }
    cnt = answer = 0
    while cnt < len(arr):
        cnt += 1
        arr.append(arr.popleft())
        # print('cnt :', cnt, 'answer :', answer, 'arr :', arr)
        
        temp = copy.deepcopy(arr)
        stack = []
        flag = True
        while len(temp):
            el = temp.popleft()
            if el in ['(', '{', '['] or not stack:
                stack.append(el)
            elif el in [')', ']', '}']:
                if stack[-1] == pair[el]:
                    stack.pop()
                else:
                    flag = False
                    break
        if stack:
            flag = False
        if flag:
            answer += 1
    return answer