from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-val for val in stones]
        heapq.heapify(stones)
        while len(stones) > 2:
            y = abs(heapq.heappop(stones))
            x = abs(heapq.heappop(stones))
            if y == x:
                continue
            heapq.heappush(stones, -(y-x))
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return abs(stones[0])
        return abs(stones[0]) - abs(stones[1])
