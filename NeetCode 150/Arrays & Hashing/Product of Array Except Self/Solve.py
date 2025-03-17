class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = []
        for i, _ in enumerate(nums):
            nums_copy = nums.copy()
            nums_copy.pop(i)
            sum = 1
            for j in nums_copy:
                sum *= j
            output.append(sum)
        return output