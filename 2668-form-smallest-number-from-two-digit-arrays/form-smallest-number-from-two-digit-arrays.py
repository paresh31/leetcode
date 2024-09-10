class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        l = list()
        for item in nums1:
            if item in nums2:
                l.append(item)
        if l: 
            return(min(l))
        n1 = min(nums1)
        n2 = min(nums2)
        return((min(n1,n2)*10) + max(n1,n2))