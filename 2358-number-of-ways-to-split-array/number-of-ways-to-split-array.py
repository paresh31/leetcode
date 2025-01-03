class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        ts = sum(nums)
        l = 0
        for i in range(n - 1):
            l += nums[i]
            r = ts - l
            if l >= r:
                res += 1
        return res

        

        