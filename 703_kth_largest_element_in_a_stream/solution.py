from heapq import heapify, heappop, heappush
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        while len(nums) > k:
            nums.pop()
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) == self.k and val < self.nums[-1]:
            return self.nums[-1]
        self.nums.append(val)
        self.nums.sort(reverse=True)
        self.nums.pop()
        return self.nums[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapify(self.minHeap)
        while len(self.minHeap) > k:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
