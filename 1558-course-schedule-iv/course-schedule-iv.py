class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        r = [[False] * numCourses for x in range(numCourses)]
        for a, b in prerequisites:
            r[a][b] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    r[i][j] = r[i][j] or (r[i][k] and r[k][j])
        return [r[u][v] for u, v in queries]