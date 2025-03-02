class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums, r = nums1 + nums2, defaultdict(int)
        for k, v in nums:
            r[k] += v
        ma = []
        for i, v in sorted(r.items()):
            ma.append([i, v])
        return ma

        