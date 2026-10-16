class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        m, n = len(mat), len(mat[0])
        row_strengths = []
        
        for i, row in enumerate(mat):
            # Binary search to count the number of 1s (soldiers) in the row
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            # Store a tuple of (soldier_count, row_index)
            row_strengths.append((left, i))
            
        # Sort tuples: Python naturally sorts by count first, then by index `i` on ties
        row_strengths.sort()
        
        # Return the indices of the first k weakest rows
        return [i for count, i in row_strengths[:k]]