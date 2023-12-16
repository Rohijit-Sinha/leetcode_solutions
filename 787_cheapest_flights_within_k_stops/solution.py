from typing import List
from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for fro,to,price in flights:
            adj[fro].append((to,price))
        cost = [float("inf") for _ in range(n)]
        cost[src] = 0
        q = deque([(-1,src,0)]) # stops,from,price
        while q:
            stops,source,total_cost = q.popleft()
            if stops == k:
                continue
            for dest,price in adj[source]:
                new_cost = total_cost + price
                if new_cost < cost[dest]:
                    cost[dest] = new_cost
                    q.append((stops+1,dest,new_cost))
        if cost[dst] < float("inf") and cost[dst]!=0:
            return cost[dst]
        return -1
            