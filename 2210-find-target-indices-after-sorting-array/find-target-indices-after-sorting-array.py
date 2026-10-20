class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less_count = 0
        eq_count = 0
        
        for x in nums:
            if x < target:
                less_count += 1
            elif x == target:
                eq_count += 1
                
        # Generate the sequence of indices directly without sorting
        return list(range(less_count, less_count + eq_count))