from typing import List
from collections import deque
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R = len(heights)
        C = len(heights[0])
        effort = [[float("inf") for _ in range(C)] for _ in range(R)]
        effort[0][0] = 0
        q = [[0,0,0]]
        change = [[-1,0],[1,0],[0,-1],[0,1]]
        heapq.heapify(q)

        while q:
            d, i,j = heapq.heappop(q)
            for ic,jc in change:
                new_i,new_j = i+ic,j+jc
                if new_i < 0 or new_i >= R or new_j < 0 or new_j >= C:
                    continue
                new_d = abs(heights[new_i][new_j] - heights[i][j])
                new_d = max(new_d,d)
                if new_d < effort[new_i][new_j]:
                    effort[new_i][new_j] = new_d
                    heapq.heappush(q,[new_d,new_i,new_j])
            if i == R-1 and j==C-1:
                return effort[R-1][C-1]
