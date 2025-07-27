class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        sd = dict(sorted(d.items(), key = lambda x: x[1], reverse = True))
        res = []
        for i, key in enumerate(sd.keys()):
            if i == k:
                break
            res.append(key)
        return res

