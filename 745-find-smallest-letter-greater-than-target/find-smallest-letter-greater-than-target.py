class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        # Instant wrap-around check
        if target >= letters[-1]:
            return letters[0]
            
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if letters[mid] <= target:
                # The target is greater or equal, search the right half
                left = mid + 1
            else:
                # The current letter is strictly greater, but there might be a smaller valid one to the left
                right = mid - 1
                
        return letters[left]