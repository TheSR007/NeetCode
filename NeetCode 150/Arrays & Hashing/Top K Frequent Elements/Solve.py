class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums = sorted(set(nums), key=lambda x: (-nums.count(x), x))
        return nums[:k]