class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        r = []  
        d = 0  
        b = {}  
        c = {}  
        for x, y in queries:
            if x in b:
                z = b[x]
                c[z] -= 1
                if c[z] == 0:
                    del c[z]
                    d -= 1
            b[x] = y
            if y in c:
                c[y] += 1
            else:
                c[y] = 1
                d += 1
            r.append(d)
        return r