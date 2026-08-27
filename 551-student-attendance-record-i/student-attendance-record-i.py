class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0

        for c in s:
            if c == 'A':
                absent += 1
                late = 0
            elif c == 'L':
                late += 1
                if late == 3:
                    return False
            else:  # P
                late = 0

            if absent == 2:
                return False

        return True