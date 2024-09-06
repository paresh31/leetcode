class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ip(sub: str) -> bool:
            return sub == sub[::-1]
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one = s[left+1:right+1]
                other = s[left:right]
                return ip(one) or ip(other)
            left += 1
            right -= 1
        
        return True