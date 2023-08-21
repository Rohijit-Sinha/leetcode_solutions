import heapq
from typing import List
import math

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [(efficiency[i], speed[i]) for i in range(len(speed))]
        engineers.sort(reverse=True)
        speedHeap = []
        speedSum = 0
        res = 0
        for i in range(len(engineers)):
            eff, sp = engineers[i]
            heapq.heappush(speedHeap, sp)
            speedSum += sp
            if len(speedHeap) > k:
                speedSum -= heapq.heappop(speedHeap)
            res = max(res, speedSum * eff)
        return res % (math.pow(10,9)+7)