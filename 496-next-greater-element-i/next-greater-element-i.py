class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_greater = {}
        
        # Traverse nums2 to find the next greater element for each number using a monotonic decreasing stack
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
            
        # Any elements left in the stack have no greater element to their right
        while stack:
            next_greater[stack.pop()] = -1
            
        # Map the results back for each element in nums1
        return [next_greater[num] for num in nums1]