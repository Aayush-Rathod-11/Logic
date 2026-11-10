class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        target = tickets[k]
        
        for i, t in enumerate(tickets):
            if i <= k:
                # People at or before index k can buy up to 'target' tickets
                time += min(t, target)
            else:
                # People after index k stop buying once the target person finishes,
                # meaning they can buy at most 'target - 1' tickets
                time += min(t, target - 1)
                
        return time