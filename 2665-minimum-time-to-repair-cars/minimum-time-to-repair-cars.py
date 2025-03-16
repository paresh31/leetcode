class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, h = 1, min(ranks) * cars * cars  
        while l < h:
            mid, total = (l + h) // 2, 0
            for r in ranks:
                total += int((mid // r) ** 0.5)
                if total >= cars:
                    break
            if total >= cars:
                h = mid
            else:
                l = mid + 1
        return l