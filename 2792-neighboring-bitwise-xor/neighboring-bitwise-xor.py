class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        d = derived
        n = len(d)    
        def c(s):
            o = [0] * n
            o[0] = s
            for i in range(1, n):
                o[i] = d[i - 1] ^ o[i - 1]
            return (o[-1] ^ o[0]) == d[-1]        
        return c(0) or c(1)