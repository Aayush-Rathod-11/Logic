class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sum_A = sum(aliceSizes)
        sum_B = sum(bobSizes)
        
        # The difference that Bob's candy needs to have compared to Alice's candy
        delta = (sum_B - sum_A) // 2
        
        # Convert Bob's sizes to a set for O(1) lookups
        set_B = set(bobSizes)
        
        for x in aliceSizes:
            if x + delta in set_B:
                return [x, x + delta]