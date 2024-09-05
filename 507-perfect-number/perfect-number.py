class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        a = 1
        i = 2
        while i * i < num:
            if num % i == 0:
                a += i + num // i
            i += 1
        if i * i == num:
            a += i
        return a == num
