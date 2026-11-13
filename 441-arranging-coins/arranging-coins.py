class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            # Total coins needed for 'mid' complete rows is (mid * (mid + 1)) // 2
            coins_needed = mid * (mid + 1) // 2
            
            if coins_needed <= n:
                ans = mid        # 'mid' rows are possible, try for more
                left = mid + 1
            else:
                right = mid - 1  # Too many coins needed, try fewer rows
                
        return ans