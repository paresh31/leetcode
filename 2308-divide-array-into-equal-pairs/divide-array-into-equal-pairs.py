class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 != 0:
            return False
        d = {}
        for item in nums:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        for v in d.values():
            if v % 2 != 0:
                return False
        return True

        
        