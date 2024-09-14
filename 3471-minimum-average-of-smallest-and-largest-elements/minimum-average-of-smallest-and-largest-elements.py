class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        a = []
        n = len(nums)
        for i in range(n//2):
            ma = max(nums)
            mi = min(nums)
            avg = (ma+mi) / 2
            a.append(avg)
            nums.remove(ma)
            nums.remove(mi)
        return(min(a))