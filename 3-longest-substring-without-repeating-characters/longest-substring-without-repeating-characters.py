class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        m = 0
        for i in range(0, n):
            c = 0
            res = []
            for j in range(i, n):
                if s[j] not in res:
                    res.append(s[j])
                    c += 1
                    m = max(m, c)
                else:
                    break
        return m
                
            
            
