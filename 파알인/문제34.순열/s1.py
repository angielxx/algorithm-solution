# 46. Permutations
# 220905

class Solution(object):
    def permute(self, nums):
        result = []
        
        def dfs(path):
            if len(path) == len(nums):
                result.append(path)
                return
            else:
                for i in range(len(nums)):
                    if nums[i] not in path:
                        dfs(path + [nums[i]])

        dfs([])
        return result

# nums = [1,2,3]
# nums = [0,1]
nums = [1]
s = Solution()
print(s.permute(nums))