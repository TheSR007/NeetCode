class Solution:
    def trap(self, height: list[int]) -> int:
        result = 0
        for i in range(1, len(height) - 1): # looping inside the boundary
            l = max(height[:i]) # left max height
            r = max(height[i:]) # right max height
            water = min(l,r) - height[i]

            if water > 0:
                result += water
        return result
