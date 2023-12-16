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
            self.size[u_par] += self.size[v_par]
        else:
            self.parent[v_par] = u_par
            self.size[v_par] += self.size[u_par]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ds = DisjointSet(len(accounts))
        mail_idx_map = {}
        for idx, mail_list in enumerate(accounts):
            for mail in mail_list[1:]:
                if mail in mail_idx_map:
                    ds.unionBySize(mail_idx_map[mail], idx)
                mail_idx_map[mail] = idx
        idx_mail_map = defaultdict(list)
        for mail, idx in mail_idx_map.items():
            par = ds.findPar(idx)
            idx_mail_map[par].append(mail)
        result = []
        for i in idx_mail_map.keys():
            lst = []
            lst.append(accounts[i][0])
            lst.extend(sorted(idx_mail_map[i]))
            result.append(lst)
        return result
