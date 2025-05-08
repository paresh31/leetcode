class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = nums[0]
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s = nums[0]
        while s != f:
            s = nums[s]
            f = nums[f]
        return s