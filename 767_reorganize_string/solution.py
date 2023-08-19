import heapq
from collections import Counter
from copy import deepcopy

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxHeap = [[-val, key] for key, val in counter.items()]
        heapq.heapify(maxHeap)
        hold = None
        res = ""
        while maxHeap:
            elem = heapq.heappop(maxHeap)
            res += elem[1]
            elem[0] += 1
            if hold:
                heapq.heappush(maxHeap, deepcopy(hold))
                hold = None
            if elem[0] < 0:
                hold = deepcopy(elem)
        if hold:
            res = ""
        return res