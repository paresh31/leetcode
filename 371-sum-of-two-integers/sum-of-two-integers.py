class Solution:
    def getSum(self, a: int, b: int) -> int:
        mx = 0xFFFFFFFF
        mk = 0x7FFFFFFF       
        while b != 0:
            c = (a ^ b) & mx
            b = (a & b) << 1
            a = c & mx
        return a if a <= mk else ~(a ^ mx)