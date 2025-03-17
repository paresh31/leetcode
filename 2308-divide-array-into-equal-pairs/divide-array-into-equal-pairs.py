class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 != 0:
            return False
        from collections import Counter
        d = dict(Counter(nums))
        for v in d.values():
            if v % 2 != 0:
                return False
        return True

        
        