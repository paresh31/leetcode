class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sm = 0
        for i in range(len(arr)):
            temp = 0
            for j in range(i, len(arr)):
                temp += arr[j]
                if abs(i - j) % 2 != 0:
                    continue
                sm += temp
        return sm