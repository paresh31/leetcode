class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums1)
        result = []
        for num in nums2:
            if count[num] > 0:
                result.append(num)
            count[num] -= 1
        return result