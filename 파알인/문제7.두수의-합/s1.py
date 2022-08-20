# 1. Two Sum
# 220820

class Solution(object):
    def twoSum(self, nums, target):
        N = len(nums)

        for i in range(N-1):
            for j in range(i+1, N):
                s = nums[i] + nums[j]
                if s == target:
                    answer = [i, j]
                    break
        return answer

nums = [3,3]
target = 6

s = Solution()
print(s.twoSum(nums, target))
