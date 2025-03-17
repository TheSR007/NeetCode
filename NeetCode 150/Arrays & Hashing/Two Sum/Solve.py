class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i is not j and num1 + num2 == target:
                    return [i,j]