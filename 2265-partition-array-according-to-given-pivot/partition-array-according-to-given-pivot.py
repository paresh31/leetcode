class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n1, n2, n3 = [], [], []
        for item in nums:
            if item < pivot:
                n1.append(item)
            elif item == pivot:
                n2.append(item)
            else:
                n3.append(item)
        return n1 + n2 + n3