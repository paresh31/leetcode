class Solution:
    def countPairs(self, arr: List[int], target: int) -> int:
        count = 0
        for i in range(len(arr)-1):
            a = arr[i]
            for j in range(i+1,len(arr)):
                b = arr[j]
                if a + b < target:
                    count += 1
        return count
