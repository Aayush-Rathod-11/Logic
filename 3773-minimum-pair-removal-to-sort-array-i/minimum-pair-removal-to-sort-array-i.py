class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        arr = list(nums)
        ans = 0
        
        def is_non_decreasing(a: list[int]) -> bool:
            for i in range(1, len(a)):
                if a[i] < a[i - 1]:
                    return False
            return True
            
        while not is_non_decreasing(arr):
            min_sum = arr[0] + arr[1]
            idx = 0
            
            # Find the adjacent pair with the minimum sum (leftmost chosen on ties)
            for i in range(1, len(arr) - 1):
                current_sum = arr[i] + arr[i + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    idx = i
            
            # Replace the pair with their sum
            arr[idx] = min_sum
            arr.pop(idx + 1)
            ans += 1
            
        return ans