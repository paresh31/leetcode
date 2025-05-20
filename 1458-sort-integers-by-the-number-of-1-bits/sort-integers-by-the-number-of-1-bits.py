class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bl = []
        for num in arr:
            bc = bin(num).count("1")
            bl.append((bc, num))
        bl.sort()
        r = [num for x, num in bl]
        return r