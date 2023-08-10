import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[point[0]**2 + point[1]**2, point[0], point[1]] for point in points]
        heapq.heapify(points)
        res = []
        while k > 0:
            tmp = heapq.heappop(points)
            res.append([tmp[1], tmp[2]])
            k -= 1
        return res