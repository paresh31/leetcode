class Solution:
    def isPalindrome(self, x: int) -> bool:
        dummy = x
        sum = 0
        while dummy > 0:
            rem = dummy % 10
            sum = (sum * 10) + rem
            dummy = dummy // 10
        if sum == x:
            return True
        else:
            return False