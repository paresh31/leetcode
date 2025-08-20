class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return []
        # r = []
        # res = set()
        # for i in range(len(s) - 9):
        #     t = s[i:i+10]
        #     if t in r:
        #         res.add(t)
        #     else:
        #         r.append(t)
        # return list(res)

        # res = []  
        # d = dict()
        # for i in range(len(s) - 9):
        #     t = s[i:i+10]
        #     if t in d and t not in res:
        #         res.append(t)
        #     else:
        #         d[t] = 1
        # return res
        seen = set()
        res = set()
        for i in range(len(s) - 9):
            t = s[i:i+10]
            if t in seen:
                res.add(t)
            else:
                seen.add(t)
        return list(res)
                




