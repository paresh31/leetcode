class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        dv = 0
        for num1 in arr1:
            fc = False
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    fc = True
                    break
            if not fc: dv += 1
        return dv