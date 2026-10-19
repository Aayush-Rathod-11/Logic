class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # x can range from 0 to n
        for x in range(n + 1):
            # Find the first index where elements are greater than or equal to x
            idx = bisect.bisect_left(nums, x)
            count = n - idx
            
            if count == x:
                return x
                
        return -1