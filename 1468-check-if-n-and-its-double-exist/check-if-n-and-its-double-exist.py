class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l = len(arr)
        for i in range(l):
            for j in range(l):
                if arr[j] * 2 == arr[i] and i != j:
                    return True
        return False