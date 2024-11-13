class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        Asum = sum(aliceSizes)
        Bsum = sum(bobSizes)

        delta = (Asum - Bsum)//2
        Ahash = set(aliceSizes)

        for number in bobSizes:
            if number + delta in Ahash:
                return [number + delta, number]