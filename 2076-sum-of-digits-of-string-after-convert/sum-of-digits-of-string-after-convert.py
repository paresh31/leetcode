class Solution:
    def getLucky(self, s: str, k: int) -> int:
        l = ''
        for item in s:
            l = l + str(ord(item) - 96)
        for j in range(k):
            a = 0
            for i in l:
                a += int(i)
            l = str(a)
        return(int(l))