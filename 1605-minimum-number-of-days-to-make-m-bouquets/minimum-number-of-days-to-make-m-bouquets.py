class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
            
        left, right = min(bloomDay), max(bloomDay)
        
        while left <= right:
            mid = (left + right) // 2
            
            bouquets = 0
            flowers = 0
            
            for day in bloomDay:
                if day <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                    
            if bouquets >= m:
                # We can make enough bouquets, try to find an earlier day
                right = mid - 1
            else:
                # We need more time, search the later days
                left = mid + 1
                
        return left