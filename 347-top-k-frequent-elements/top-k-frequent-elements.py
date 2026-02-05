class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        d = dict(Counter(nums))
        r = dict(sorted(d.items(), key = lambda x: x[1], reverse = True))
        a = []
        for i, key in enumerate(r.keys()):
            if i == k: break
            a.append(key)
        return a

