class Solution:
    def isPalindrome(self, x: int) -> bool:
        # dummy, sum = x, 0
        # while dummy > 0:
        #     rem = dummy % 10
        #     sum = (sum * 10) + rem
        #     dummy = dummy // 10
        # if sum == x:
        #     return True
        # else:
        #     return False

        # if x < 0:
        #     return False
        # s = int(str(x)[::-1])
        # return s == x

        if x < 0:
            return False
        s = int(str(x)[::-1])
        return s == x



        
