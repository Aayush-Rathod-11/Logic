import bisect
import itertools

class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # Sort nums to pick the smallest elements first for maximum subsequence size
        nums.sort()
        
        # Compute prefix sums of the sorted array
        prefix_sums = list(itertools.accumulate(nums))
        
        # For each query, use binary search to find how many elements fit within the limit
        return [bisect.bisect_right(prefix_sums, q) for q in queries]