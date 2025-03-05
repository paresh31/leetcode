class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        mi, mx = nums[0], nums[-1]
        for i in range(mi, 0, -1):
            if mi % i == 0 and mx % i == 0:
                return i