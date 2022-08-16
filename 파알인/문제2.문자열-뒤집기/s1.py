# 344. Reverse String
# 220815

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        N = len(s)

        for i in range(N // 2):
            s[i], s[(i+1) * (-1)] = s[(i+1) * (-1)], s[i]
