class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        diff = xor & -xor
        res = [0, 0]
        for n in nums:
            if n & diff:
                res[0] ^= n
            else:
                res[1] ^= n
        return res