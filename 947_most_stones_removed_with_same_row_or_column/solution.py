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
    def removeStones(self, stones: List[List[int]]) -> int:
        maxRow, maxCol = max([el[0] for el in stones]), max([el[1] for el in stones])
        ds = DisjointSet(maxRow + maxCol + 2)
        store = set()
        for row, col in stones:
            nodeRow = row
            nodeCol = col + maxRow + 1
            ds.unionBySize(nodeRow, nodeCol)
            store.add(nodeRow)
            store.add(nodeCol)
        cnt = 0
        for node in store:
            if ds.findPar(node) == node:
                cnt += 1
        return len(stones) - cnt
