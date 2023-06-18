def solution(s):
    
    
    def is_pal(str):
        for i in range(len(str) // 2):
            if str[i] != str[i * (-1)]:
                return False
        return True
    
    answer = 1
    # start,end = 0,1
    # print(s[start:end])
    # 홀수
    def find(start, end):
        answer = 0
        while end < len(s):
            if is_pal(s[start:end]):
                l, r = start, end
                length = 0
                while 0 <= l and r <= len(s) and s[l] == s[r-1]:
                    if s[l] == s[r-1]:
                        length = r - l
                        l -= 1
                        r += 1
                if length > answer: answer = length
            start += 1
            end += 1
        return answer
    a = find(0,1)
    b = find(0,2)
    answer = max(a, b, answer)
    return answer
    