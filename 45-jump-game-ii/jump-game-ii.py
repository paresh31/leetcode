class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        j, c, m = 0, 0, 0
        for i in range(n-1):
            m = max(m, i + nums[i])
            if i == c:
                j += 1
                c = m
        return j