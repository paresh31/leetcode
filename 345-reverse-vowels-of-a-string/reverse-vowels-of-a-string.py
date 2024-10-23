class Solution:
    def reverseVowels(self, s: str) -> str:
        l=['a','e','i','o','u','A','E','I','O','U']
        m=[]
        for i in s:
            if i in l:
                m.append(i)
        n=len(m)
        s=list(s)
        for i in range(len(s)):
            if s[i] in l:
                n-=1
                s[i]=m[n]
        return ''.join(s)