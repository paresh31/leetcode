class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        r = {}
        for i, v in nums1:
            if i in r:
                r[i] += v
            else:
                r[i] = v
        for i, v in nums2:
            if i in r:
                r[i] += v
            else:
                r[i] = v
        s = sorted(r.keys())
        ma = []
        for i in s:
            ma.append([i, r[i]])
        return ma

        