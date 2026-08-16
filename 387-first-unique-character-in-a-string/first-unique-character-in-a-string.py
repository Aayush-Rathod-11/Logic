class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [0] * 26

        for c in s:
            count[ord(c) - 97] += 1

        for i, c in enumerate(s):
            if count[ord(c) - 97] == 1:
                return i

        return -1