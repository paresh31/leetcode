class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        s1.extend(s2)
        d,s = set(), set()
        for item in s1:
            if item not in s:
                s.add(item)
            else:
                d.add(item)
        for i in d:
            if i in s:
                s.remove(i)
        return(s)   