# 15. 3Sum
# 220820

# Time Limit Exceeded

class Solution(object):
    def threeSum(self, nums):
        target = 0
        combi = []
        nums_map = { n : i for i, n in enumerate(nums)}
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        if temp not in combi:
                            combi.append(temp)
        return combi

nums = [-1,0,1,2,-1,-4] # 6
s = Solution()
print(s.threeSum(nums))