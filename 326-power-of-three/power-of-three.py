class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        t = False
        for i in range(n):
            if 3**i == n:
                t = True
                break
            if 3**i > n:
                break
        return t