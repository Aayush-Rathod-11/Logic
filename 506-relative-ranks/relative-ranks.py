class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        ans = [""] * n
        medals = ("Gold Medal", "Silver Medal", "Bronze Medal")

        # Pair each score with its original index and sort descending
        ranked = sorted(enumerate(score), key=lambda x: x[1], reverse=True)

        for rank, (idx, _) in enumerate(ranked):
            ans[idx] = medals[rank] if rank < 3 else str(rank + 1)

        return ans  