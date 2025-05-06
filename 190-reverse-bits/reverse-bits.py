class Solution:
    def reverseBits(self, n: str) -> int:
        # n = format(n, 'b')
        # n = n.zfill(32)
        # r = n[::-1]
        # res = int(r, 2)
        # return res

        res = 0
        for i in range(32):
            res = res << 1 | (n & 1)
            n >>= 1
        return res