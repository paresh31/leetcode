class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        r = n
        for i in range(n):
            r = r ^ i
            r = r ^ nums[i]
        return r