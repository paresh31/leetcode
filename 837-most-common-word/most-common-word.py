import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cp = re.sub(r'[^A-Za-z0-9\s]', ' ', paragraph)
        p = cp.lower()
        l = p.split()
        l = [word for word in l if word not in banned]
        c = 0
        s = ""
        for item in set(l):
            if l.count(item) > c:
                c = l.count(item)
                s = item
        return(s)