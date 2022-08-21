# 238. Product of Array Except Self
# 220821

class Solution(object):
    def productExceptSelf(self, nums):
        result = []
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    total *= nums[j]
            result.append(total)
        return result
nums = [-1,1,0,-3,3]
s = Solution()
print(s.productExceptSelf(nums))