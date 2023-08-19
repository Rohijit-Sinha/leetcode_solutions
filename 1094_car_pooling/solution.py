from typing import List
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickHeap = []
        dropHeap = []
        for pa, fr, to in trips:
            pickHeap.append([fr, pa])
            dropHeap.append([to, pa])
        heapq.heapify(pickHeap)
        heapq.heapify(dropHeap)
        cur = 0
        while pickHeap:
            pickFrom, pickPa = heapq.heappop(pickHeap)
            while dropHeap and dropHeap[0][0] <= pickFrom:
                _, dropPa = heapq.heappop(dropHeap)
                cur -= dropPa
            cur += pickPa
            if cur > capacity:
                return False
        return True