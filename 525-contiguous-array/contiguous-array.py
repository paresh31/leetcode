class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        s = 0
        res = 0
        for i, v in enumerate(nums):
            if v == 0:
                s += -1
            else:
                s += 1
            if s in d:
                res = max(res, i - d[s])
            else:
                d[s] = i
        return res
