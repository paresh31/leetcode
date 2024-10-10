class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        mxr = [0] * len(nums)
        i = len(nums) - 1
        prm = 0
        for n in reversed(nums):
            mxr[i] = max(n, prm)
            prm = mxr[i]
            i -= 1
        res = 0
        l = 0
        for r in range(len(nums)):
            while nums[l] > mxr[r]:
                l += 1
            res = max(res, r - l)
        return res
        