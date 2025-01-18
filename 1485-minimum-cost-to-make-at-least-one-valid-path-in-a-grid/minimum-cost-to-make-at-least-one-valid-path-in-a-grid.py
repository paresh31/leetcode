class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        store = [[inf]*n for _ in range(m)]
        store[0][0] = 0
        cur,nex,cost = deque([(0,0)]),deque(),0
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        while store[-1][-1]>=cost:
            while cur:
                i,j = cur.popleft()
                for t in range(4):
                    x,y = d[t]
                    if -1<x+i<m and -1<y+j<n:
                        if t==grid[i][j]-1:
                            if store[i+x][j+y]>cost:
                                store[i+x][j+y] = cost
                                cur.append((i+x,y+j))
                        else:
                            if store[i+x][j+y]>cost+1:
                                store[i+x][j+y] = cost+1
                                nex.append((i+x,y+j))
            cur = nex
            cost += 1
            nex = deque()
        return store[-1][-1]