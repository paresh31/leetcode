class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for item in nums:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        for k, v in d.items():
            if d[k] == 1:
                return k