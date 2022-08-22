# 15. 3Sum
# 220820

# Time Limit Exceeded

class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()

        # 브루트포스 n^3 반복
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기(첫번째수 중복되면 같은 조합을 가진 경우의 수가 생감)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 sum 계산
            # 첫번째 left, right 설정
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0인 경우
                    result.append([nums[i], nums[left], nums[right]])

                    # 같은 값이 연달아 나오는 경우 left, right를 한번 더 바꿔준다
                    # 2개, 3개 이상의 연속된 숫자가 있을 수 있으므로 while문 사용
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

nums = [-1,0,1,2,-1,-4] # 6
s = Solution()
print(s.threeSum(nums))