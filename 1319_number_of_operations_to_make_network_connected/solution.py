from typing import List

class DisjointSet:
    def __init__(self, n: int) -> None:
        self.size = [1 for _ in range(n)]
        self.parent = [i for i in range(n)]

    def findPar(self, node: int):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u: int, v: int):
        u_par = self.findPar(u)
        v_par = self.findPar(v)
        if u_par == v_par:
            return
        if self.size[u_par] < self.size[v_par]:
            self.parent[u_par] = v_par
            self.size[u_par] += self.size[v_par]
        else:
            self.parent[v_par] = u_par
            self.size[v_par] += self.size[u_par]


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        extra = 0
        compo = 0    
        for u, v in connections:
            if ds.findPar(u) == ds.findPar(v):
                extra += 1
            else:
                ds.unionBySize(u,v)
        for node in range(n):
            if ds.findPar(node) == node:
                compo += 1
        if compo - 1 <= extra:
            return compo - 1
        return -1