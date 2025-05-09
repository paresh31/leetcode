class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # t = False
        # for i in range(n):
        #     if 4**i == n:
        #         t = True
        #         break
        #     if 4**i > n:
        #         break
        # return (t)        



        if n <= 0:
            return False
        if (n & (n - 1)) != 0:
            return False
        if (n & 0x55555555) == 0:
            return False
        return True