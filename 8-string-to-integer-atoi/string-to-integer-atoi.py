class Solution:
    def myAtoi(self, s: str) -> int:
        ls = s.lstrip()
        ls = list(''.join(ls))
        n = ''
        sy = ''
        imx = 2**31 - 1
        imn = -2**31
        if len(ls) == 0:
            return 0
        if ls[0] == '-' or ls[0] == '+':
            sy = ls.pop(0)
        for itm in ls:
            if itm.isnumeric():
                n += itm
            else:
                break
        if len(n) == 0:
            return 0
        res = int(n)
        if sy == '-':
            res = -res
        if res > imx:
            return imx
        elif res < imn:
            return imn
        return res