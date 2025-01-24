class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        h = {}
        def d(x):
            if x in h:
                return h[x]
            h[x] = False

            for y in graph[x]:
                if not d(y):
                    return False
            h[x] = True
            return h[x]
        r = []
        for i in range(n):
            if d(i):
                r.append(i)
        return r