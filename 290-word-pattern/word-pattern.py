class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()
        if len(pattern) != len(s):
            return(False)
        if len(set(s)) != len(set(pattern)):
            return(False)
        dict = {}
        for i in range(len(s)):
            dict.update({pattern[i]: s[i]})
        for i in range(len(s)):
            if s[i] != dict.get(pattern[i]):
                return(False)
        return(True)
                    
            