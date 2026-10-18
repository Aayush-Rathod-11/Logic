class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Number of missing integers up to the current index `mid`
            missing_count = arr[mid] - (mid + 1)
            
            if missing_count < k:
                # We need more missing numbers, search the right half
                left = mid + 1
            else:
                # Too many missing numbers, search the left half
                right = mid - 1
                
        # When the loop terminates, `left` points to the correct position, 
        # and the kth missing number is simply `left + k`
        return left + k