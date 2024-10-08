class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        li = list()
        for i in range(len(nums)):
            if nums[i] == target:
                li.append(i)
        if len(li) == 0:
            return [-1,-1]
        return [li[0], li[-1]]