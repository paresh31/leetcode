class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = []
        n = len(grid[0])
        for i in range(n):
            for j in range(n):
                l.append(grid[i][j])
        r,m = 0,0
        for i in range(0, len(l)):
            if i+1 not in l:
                m = i+1
            if l.count(l[i]) == 2:
                r = l[i]
        return(r,m) 