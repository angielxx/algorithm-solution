# 42. Trapping Rain Water
# 220820

class Solution(object):
    def trap(self, height):
        stack = []
        volume = 0

        for i in range(len(height)):
            print(stack)
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break
                print(i)
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume

# height = [0,2,0]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(height))