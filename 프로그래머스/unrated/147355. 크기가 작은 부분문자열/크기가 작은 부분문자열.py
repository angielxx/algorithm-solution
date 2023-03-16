def solution(t, p):
    l = len(p)
    s = 0
    cnt = 0
    arr = []
    while s + l <= len(t):
        e = s + l
        num = int(t[s:e])
        if num <= int(p):
            cnt += 1
            arr.append(num)
        s += 1
    return cnt