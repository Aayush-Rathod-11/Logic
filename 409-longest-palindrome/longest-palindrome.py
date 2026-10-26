class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        length = 0
        
        for char in s:
            if char in seen:
                # Found a pair, remove it from the set and add 2 to the length
                seen.remove(char)
                length += 2
            else:
                # Character doesn't have a pair yet, record it
                seen.add(char)
                
        # If there are any unpaired characters left, we can place one in the center
        return length + 1 if seen else length