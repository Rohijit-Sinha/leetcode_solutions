from typing import List
import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        tasks = [-cnt for cnt in counter.values()]
        heapq.heapify(tasks)
        queue: "deque[List[int]]" = deque([])
        time = 0
        while tasks or queue:
            time += 1
            if tasks:
                count = heapq.heappop(tasks)
                count += 1
                if count < 0:
                    queue.append([count, time + n])
            if queue and queue[0][1] == time:
                queu_task = queue.popleft()
                heapq.heappush(tasks, queu_task[0])
        return time
