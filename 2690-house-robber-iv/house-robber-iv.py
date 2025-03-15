class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, h = min(nums), max(nums)
        while l < h:
            m = (l + h) // 2
            c, i = 0, 0
            while i < len(nums):
                if nums[i] <= m:
                    c += 1
                    i += 1
                i += 1
            if c >= k:
                h = m
            else:
                l = m + 1
        return l