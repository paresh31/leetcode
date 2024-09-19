class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        nc = {}
        res = []
        for n in names:
            if n not in nc:
                res.append(n)
                nc[n] = 1
            else:
                k = nc[n]
                while n + f"({k})" in nc:
                    k += 1
                new_name = n + f"({k})"
                res.append(new_name)
                nc[n] = k + 1
                nc[new_name] = 1
        return res