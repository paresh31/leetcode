class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        el = []
        for i in range(len(arr2)):
            a = arr1.count(arr2[i])
            for j in range(a):
                el.append(arr2[i])
        el2 = []
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                el2.append(arr1[i])
        el2.sort()
        return (el + el2)