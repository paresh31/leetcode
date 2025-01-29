class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        def union(u,v):
            ult_u = find(u)
            ult_v = find(v)
            if ult_u == ult_v:
                return False
            if size[ult_u] > size[ult_v]:
                parent[ult_v] = ult_u
                size[ult_u] += size[ult_v]
            else:
                parent[ult_u] = ult_v
                size[ult_v] += size[ult_u]
            return True

        n = len(edges)
        size = [1] * (n+1)
        parent = [0] * (n+1)
        for i in range(n+1):
            parent[i] = i
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        return 


        