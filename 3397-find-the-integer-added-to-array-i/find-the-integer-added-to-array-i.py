class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        l = len(nums1)
        s1 = sum(nums1)
        s2 = sum(nums2)
        return((s2//l) - (s1//l))