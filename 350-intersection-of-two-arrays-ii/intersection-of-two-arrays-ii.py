class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}

        for x in nums1:
            count[x] = count.get(x, 0) + 1

        result = []

        for x in nums2:
            if count.get(x, 0) > 0:
                result.append(x)
                count[x] -= 1

        return result