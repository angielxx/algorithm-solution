# 42. Trapping Rain Water
# 220820

# Time Limit Exceeded

class Solution(object):
    def trap(self, height):
        N = len(height)

        # 젤 높은 기둥 찾기
        highest = 0
        highest_idx = 0
        for i in range(N):
            if height[i] > highest:
                highest_idx = i
                highest = height[i]
        # 앞쪽
        start = 0
        for i in range(N):
            if height[i] > 0:
                start = i
                h1 = height[i]
                break
        h2 = 0
        rain = 0
        end = start
        while True:
            if start == highest_idx:
                break
            for i in range(start+1, highest_idx+1):
                if height[i] >= h1:
                    h2 = height[i]
                    end = i
                    break
            for j in range(start, end):
                rain += (h1 - height[j])
            h1 = h2
            start = end

        # 뒤쪽
        start = 0
        for i in range(N-1, highest_idx, -1):
            if height[i] > 0:
                start = i
                h1 = height[i]
                break
        h2 = 0
        while True:
            if start == highest_idx:
                break
            for i in range(start-1, highest_idx-1, -1):
                if height[i] >= h1:
                    h2 = height[i]
                    end = i
                    break
            for j in range(start, end, -1):
                rain += (h1 - height[j])
            h1 = h2
            start = end
        return rain

height = [0,2,0]
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(height))