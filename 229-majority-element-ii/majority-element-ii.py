class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)/3
        l =[]
        for item in nums:
            if item not in l and nums.count(item) > n:
                l.append(item)
        return l