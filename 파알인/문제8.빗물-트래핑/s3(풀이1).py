# 42. Trapping Rain Water
# 220820

class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            print('point', left, right)
            print('max', left_max, right_max)
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            print('max', left_max, right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
            print('vol', volume)
        return volume

# height = [0,2,0]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(height))