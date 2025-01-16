class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x1, x2 = 0, 0
        for a in nums1:
            x1 ^= a
        for b in nums2:
            x2 ^= b
        return (len(nums2) % 2) * x1 ^ (len(nums1) % 2) * x2