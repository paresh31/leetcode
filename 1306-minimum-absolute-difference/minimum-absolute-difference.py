class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums = arr.copy()
        nums.sort()
        minimum_diff = float('inf')
        pairs = []
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            
            if diff == minimum_diff:
                pairs.append([nums[i], nums[i+1]])
            elif diff < minimum_diff:
                minimum_diff = diff
                pairs = [[nums[i], nums[i+1]]]
        
        return pairs
