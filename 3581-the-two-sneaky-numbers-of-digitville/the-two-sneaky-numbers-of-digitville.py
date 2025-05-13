class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        for item in nums:
            d[item] = d.get(item, 0) + 1
        res = []
        for k, v in d.items():
            if v == 2:
                res.append(k)
        return res