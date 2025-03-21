class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # l = [-1]
        # for i in arr:
        #     if i == arr.count(i):
        #         l.append(i)
        # return(max(l))

        d = {}
        for item in arr:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        res = []
        for k, v in d.items():
            if k == v:
                res.append(v)
        if res:
            return max(res)
        return -1