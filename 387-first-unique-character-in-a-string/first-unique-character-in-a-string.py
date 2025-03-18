class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for item in s:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        for i, v in enumerate(s):
            if d[v] == 1:
                return i
        return -1


        