class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n must be positive
        # n must be a power of two: (n & (n - 1) == 0)
        # The single set bit must be at an even bit position (masked with 0x55555555)
        return n > 0 and (n & (n - 1) == 0) and (n & 0x55555555) != 0