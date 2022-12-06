class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        Graph = collections.defaultdict(list)

        for a,b in edges:
            Graph[a].append(b)
            Graph[b].append(a)

        visited = set()
        res = 0

        for v in Graph.keys():
            if v not in visited:
                visited.add(v)
                stack = [v]
                while stack:
                    g = stack.pop()
                    for z in Graph[g]:
                        if z not in visited:
                            stack.append(z)
                            visited.add(z)
                res += 1
        return res + (n-len(Graph))