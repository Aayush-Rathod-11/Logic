class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        result = n

        for i, num in enumerate(nums):
            result ^= i ^ num

        return result
