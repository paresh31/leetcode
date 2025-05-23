class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        s = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            s += 1
        r = left << s
        return r