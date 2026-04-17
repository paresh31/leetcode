class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        neg = 1
        if s[0] == "-":
            neg = -1
            s = s[1:]
        rev = ""
        for item in s:
            rev = item + rev
        res = neg * int(rev)
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return(res)
        

        