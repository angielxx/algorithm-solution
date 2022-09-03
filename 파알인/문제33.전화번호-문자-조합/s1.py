# 17. Letter Combinations of a Phone Number
# 220903

# PASS

class Solution(object):
    def letterCombinations(self, digits):
        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        subset = []
        for n in digits:
            if not subset:
                subset += letters[n]
            else:
                temp = subset
                stack = []
                for letter in letters[n]:
                    for i in range(len(temp)):
                        stack.append(temp[i] + letter)
                subset = stack
        return subset
            

digits = "234"
s = Solution()
print(s.letterCombinations(digits))