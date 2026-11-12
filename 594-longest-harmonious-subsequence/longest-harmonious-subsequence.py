from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        count = Counter(nums)
        max_len = 0
        
        for num in count:
            # Check if num + 1 exists in our frequency map
            if num + 1 in count:
                current_len = count[num] + count[num + 1]
                if current_len > max_len:
                    max_len = current_len
                    
        return max_len