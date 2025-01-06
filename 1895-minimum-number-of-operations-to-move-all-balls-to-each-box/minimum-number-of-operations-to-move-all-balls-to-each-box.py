class Solution:
    def minOperations(self, b: str) -> List[int]:
        n = len(b)
        lm = [0] * n
        rm = [0] * n        
        c = 0
        m = 0
        for i in range(n):
            lm[i] = m
            if b[i] == '1':
                c += 1
            m += c        
        c = 0
        m = 0
        for i in range(n-1, -1, -1):
            rm[i] = m
            if b[i] == '1':
                c += 1
            m += c        
        return [lm[i] + rm[i] for i in range(n)]