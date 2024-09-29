class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        a = []
        s = 0
        count = 0
        for item in nums:
            s += item
            if s > 0:
                count += 1
            else:
                break
        return count

        
        
