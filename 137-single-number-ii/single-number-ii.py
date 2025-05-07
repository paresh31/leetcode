class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for item in nums: d[item] = d.get(item, 0) + 1
        for k, v in d.items():
            if d[k] != 3:
                return k