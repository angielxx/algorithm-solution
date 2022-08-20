# 5. Longest Palindromic Substring
# 220819

# Time Limit Exceeded

class Solution(object):
    def longestPalindrome(self, s):

        if len(s) == 1:
            return s
        else:
            start = 0
            end = 0
            max = 0
            max_slice = ''
            while start < len(s):
                while end < len(s):
                    slice = s[start:end+1]
                    if slice == slice[::-1]:
                        if len(slice) >= max:
                            max = len(slice)
                            max_slice = slice
                    end += 1
                start += 1
                end = start+1
            return max_slice

solution = Solution()
print(solution.longestPalindrome("ccc"))