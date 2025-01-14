class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0] * n
        seen_A = set()
        seen_B = set()
        for i in range(n):
            seen_A.add(A[i])
            seen_B.add(B[i])
            C[i] = len(seen_A & seen_B)
        return C