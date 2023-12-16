from typing import List
from collections import defaultdict, deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for to, from_list in enumerate(graph):
            for fro in from_list:
                adj[fro].append(to)
        ingrades = defaultdict(int)
        for _, nodes in adj.items():
            for node in nodes:
                ingrades[node] += 1

        q = deque([])
        for i in range(len(graph)):
            if len(adj[i]) == 0:
                q.append(i)
        res = []
        while q:
            node = q.popleft()
            for nei in adj[node]:
                ingrades[nei] -= 1
                if ingrades[nei] == 0:
                    q.append(nei)
            res.append(node)
        return res