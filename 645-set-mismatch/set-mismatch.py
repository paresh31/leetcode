class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        di = dict()
        for item in nums:
            di[item] = di.get(item, 0) + 1
        res = []
        for key, value in di.items():
            if value == 2: res.append(key)
        for i in range(1, n+1):
            if i not in di: res.append(i)
        return res