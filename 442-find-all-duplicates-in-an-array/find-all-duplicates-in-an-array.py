class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        res = []
        for k, v in d.items():
            if v == 2:
                res.append(k)
        return res