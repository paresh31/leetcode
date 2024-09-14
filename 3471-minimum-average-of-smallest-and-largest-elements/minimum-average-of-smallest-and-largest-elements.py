class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        l = []
        for i in range(n//2):
            l.append((nums[0]+nums[-1])/2)
            nums.pop(0)
            nums.pop(-1)
        return(min(l))