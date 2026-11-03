class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        # Count the frequency of each student preference (0s and 1s)
        counts = [0, 0]
        for s in students:
            counts[s] += 1
            
        # Process sandwiches from top to bottom
        for sandwich in sandwiches:
            if counts[sandwich] > 0:
                # A student exists who prefers this sandwich; they take it and leave
                counts[sandwich] -= 1
            else:
                # No remaining students want this sandwich type, process halts
                break
                
        # The sum of remaining preferences represents students unable to eat
        return sum(counts)