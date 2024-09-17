class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []  
        seen = []  
        for w in strs:
            s_w = ''.join(sorted(w))
            if s_w in seen:
                idx = seen.index(s_w)
                res[idx].append(w)
            else:
                seen.append(s_w)
                res.append([w])
        return res