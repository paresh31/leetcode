class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        r = []
        for i in range(len(nums)):
            l = nums[i+1:]
            if l:
                l_max = max(l)
                if l_max > nums[i]:
                    r.append(l_max - nums[i])
        if r:
            return(max(r))
        return -1