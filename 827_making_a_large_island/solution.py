from typing import List
from collections import defaultdict


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
            self.size[v_par] += self.size[u_par]
        else:
            self.parent[v_par] = u_par
            self.size[u_par] += self.size[v_par]

    def getSize(self, par: int):
        return self.size[par]


class Solution:
    def isValid(self, r: int, c: int):
        return r >= 0 and r < self.gridLen and c >= 0 and c < self.gridWidth

    def getVal(self, r: int, c: int):
        return (r * self.gridLen) + c

    def largestIsland(self, grid: List[List[int]]) -> int:
        self.gridLen = len(grid)
        self.gridWidth = len(grid[0])

        ds = DisjointSet(self.gridLen * self.gridLen)
        row_tra = [-1, 1, 0, 0]
        col_tra = [0, 0, -1, 1]
        for row in range(self.gridLen):
            for col in range(self.gridWidth):
                if grid[row][col] == 0:
                    continue
                num = self.getVal(row, col)
                for i in range(len(row_tra)):
                    new_row, new_col = row + row_tra[i], col + col_tra[i]
                    if self.isValid(new_row, new_col) and grid[new_row][new_col] == 1:
                        new_num = self.getVal(new_row, new_col)
                        ds.unionBySize(num, new_num)

        res = 0
        for row in range(self.gridLen):
            for col in range(self.gridWidth):
                if grid[row][col] == 1:
                    continue
                nei_set = set()
                for i in range(len(row_tra)):
                    new_row, new_col = row + row_tra[i], col + col_tra[i]
                    if self.isValid(new_row, new_col) and grid[new_row][new_col] == 1:
                        new_num = self.getVal(new_row, new_col)
                        nei_set.add(ds.findPar(new_num))
                size = 0
                for par in nei_set:
                    size += ds.getSize(par)
                res = max(size + 1, res)

        if res == 0:
            res = len(grid) * len(grid)

        # for each in range(len(grid) * len(grid)):
        #     res = max(res, ds.size[each])
        return res
