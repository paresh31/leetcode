class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        l = [0,1]
        a,b = l[-1], l[-2]
        for i in range(n-1):
            c = a + b
            l.append(c)
            a = l[-1]
            b = l[-2]
        return(l[-1])

