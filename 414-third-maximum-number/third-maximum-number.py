class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        li = sorted(set(nums))
        if len(li) == 2:
            return li[-1]
        if len(li) == 1:
            return li[0]
        return li[-3]
