class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        cnt=0
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                cnt+=1
        if nums[0]<nums[n-1]:
            cnt+=1
        return cnt<=1