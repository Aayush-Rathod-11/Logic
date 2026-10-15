class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c = m - 1, 0
        count = 0
        
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                # If this element is negative, all elements to its right 
                # in this row are also negative.
                count += n - c
                # Move up to check the next row
                r -= 1
            else:
                # If it's positive or zero, move right to find the negatives
                c += 1
                
        return count