class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import deque
        d = deque(nums)
        d.rotate(k)
        nums[:] = list(d)