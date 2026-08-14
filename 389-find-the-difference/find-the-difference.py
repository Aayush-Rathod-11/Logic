class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0

        for c in s:
            ans ^= ord(c)

        for c in t:
            ans ^= ord(c)

        return chr(ans)