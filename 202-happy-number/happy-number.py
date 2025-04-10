class Solution:
    def isHappy(self, n: int) -> bool:
        # if n%9==1 or n%9==7:
        #     return True
        # return False
        hashmap = {}
        while True:
            temp = sum(int(i)**2 for i in str(n))
            if int(temp) == 1:
                return True
            if temp in hashmap:
                return False
            hashmap[temp] = 1
            n = temp
        