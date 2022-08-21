# 561. Array Partition
# 220821

class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        sum = 0

        # 0 2, 2,4, 4,6
        for i in range(len(nums)//2):
            sum += nums[2*i]
        return sum

nums = [1,4,3,2]
# nums = [1, 2, 2, 5, 6, 6]

s = Solution()
print(s.arrayPairSum(nums))