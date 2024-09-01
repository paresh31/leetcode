class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        new_list = []
        s = 0
        t = 0  
        for i in range(0, m):
            t += n 
            l = original[s:t]
            new_list.append(l)
            s += n
        return new_list
            