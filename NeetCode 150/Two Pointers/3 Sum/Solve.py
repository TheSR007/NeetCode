class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        for i in range (0, len(nums)):
            for j in range (i + 1, len(nums)):
                for k in range (j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append(sorted([nums[i], nums[j], nums[k]]))

        unique_sublists = set(tuple(sublist) for sublist in result) # making Unique Sublists

        return [list(sublist) for sublist in unique_sublists] # Converting back to list