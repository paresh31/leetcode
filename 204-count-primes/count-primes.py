class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        p = [True] * (n + 1)
        p[0] = p[1] = False
        for i in range(2, int(n**0.5) + 1):
            if p[i]:
                for j in range(i+i, n+1, i):
                    p[j] = False
        pnos = []
        for i in range(n):
            if p[i]:
                pnos.append(i)
        return len(pnos)
                
