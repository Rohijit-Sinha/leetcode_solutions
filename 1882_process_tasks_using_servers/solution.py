from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        servers = [(val, idx) for idx, val in enumerate(servers)]
        heapq.heapify(servers)
        occupied = [] # (wairt_till, weight, index)
        res = [-1] * len(tasks)
        timer = 0
        for i in range(len(tasks)):
            timer = max(i, timer) # if there is a jump in timer due to no servers, several tasks will be enqueued at once.
                                  # this makes sure timer remains the same if timer > i and increases if i > timer. 
            if len(servers) == 0:
                timer = occupied[0][0]
            while occupied and occupied[0][0] <= timer:
                wait, weight, idx = heapq.heappop(occupied)
                heapq.heappush(servers, (weight, idx))
            
            weight, index = heapq.heappop(servers)
            res[i] = index
            heapq.heappush(occupied, (timer+tasks[i],weight, index))

        return res