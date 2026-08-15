class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        chars = "0123456789abcdef"
        result = ""

        num &= 0xFFFFFFFF

        while num:
            result = chars[num & 15] + result
            num >>= 4

        return result