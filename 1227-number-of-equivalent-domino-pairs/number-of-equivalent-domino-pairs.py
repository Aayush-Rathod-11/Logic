from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        counts = defaultdict(int)
        pairs = 0

        for a, b in dominoes:
            # Canonicalize orientation so [a, b] and [b, a] map to the same key
            key = (a, b) if a <= b else (b, a)
            pairs += counts[key]
            counts[key] += 1

        return pairs