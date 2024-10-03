class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        mx = 0
        for item in nums:
            if item == 1:
                count += 1
            else:
                mx = max(mx, count)
                count = 0
            mx = max(mx, count)
        return mx
        

