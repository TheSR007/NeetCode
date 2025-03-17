class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        result = 1
        current_streak = 1
        
        nums = sorted(set(nums)) # making nums sorted and Unique list
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:  # If current number is consecutive
                current_streak += 1  # Increment the current streak
            else:
                result = max(result, current_streak)  # Update the result if needed
                current_streak = 1  # Reset the streak for a new sequence
        
        return max(result, current_streak)  # Return the longest streak