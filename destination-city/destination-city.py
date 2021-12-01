class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for path in paths:
            a, b = path
            d[a] = d.get(a, 0) + 1
            d[b] = d.get(b, 0)
        for x in d:
            if d[x] == 0:
                return x
