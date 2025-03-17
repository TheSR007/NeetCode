class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1 # left and right index 
        result = 0

        for _ in range (len(heights)):
            area = min(heights[l], heights[r]) * (r - l) # min height * width
            result = max(area, result)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result
