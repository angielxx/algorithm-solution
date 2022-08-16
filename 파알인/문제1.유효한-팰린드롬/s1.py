# 125. Valid Palindrome
# 220815

"""
틀린 테스트케이스
tc1 = "0z;z   ; 0"
tc1 = "0P"
tc3 = "a."

틀린부분
while문에서 len(s)로함 (tc1)
문자열의 길이가 1인 경우, index error (tc3)
숫자도 리스트안에 넣어야함 (tc2)
"""

class Solution(object):
    def isPalindrome(self, s):
        s_list = list()

        for char in s:
            if char.isalpha() or char.isdigit():
                char = char.lower()
                s_list.append(char)

        result = True
        if len(s_list) == 1:
            pass
        elif len(s_list) > 1:
            i = 0
            while i <= len(s_list) // 2:
                if s_list[i] == s_list[(i + 1) * (-1)]:
                    i += 1
                else:
                    result = False
                    break
        return result