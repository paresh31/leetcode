class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        result = prices[:]
        
        for i in range(n):
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                result[idx] -= prices[i]
            stack.append(i)
        
        return result