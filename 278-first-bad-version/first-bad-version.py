# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                # The first bad version is at mid or earlier
                right = mid
            else:
                # The first bad version is strictly after mid
                left = mid + 1
                
        return left