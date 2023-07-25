def solution(number, k):
    stack = []
    
    i = 0
    while i < len(number):
        n = int(number[i])
        if stack:
            while stack and k and stack[-1] < n:
                stack.pop()
                k -= 1
        stack.append(n)
        i += 1
    return ''.join(list(map(str, stack[:len(stack) - k])))