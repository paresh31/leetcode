class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        r = list()
        for i in range(1, len(nums), 2):
            r.append(min(nums[i], nums[i - 1]))
        return sum(r)