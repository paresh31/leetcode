class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li = list()
        for item in nums1:
            if item in nums2 and item not in li:
                li.append(item)
        return li