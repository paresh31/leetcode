class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        w1 = s1.split()
        w2 = s2.split()
        if len(w1) < len(w2):
            w1, w2 = w2, w1
        st, e = 0, 0
        n1, n2 = len(w1), len(w2)
        while st < n2 and w1[st] == w2[st]:
            st += 1
        while e < n2 and w1[n1 - e - 1] == w2[n2 - e - 1]:
            e += 1
        return st + e >= n2
        