from typing import List
import heapq

# class Solution:
#     def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
#         nums2 = list(zip(nums2, nums1)) # [(num2, num1),...]
#         nums2.sort()
#         nums1 = [num[1] for num in nums2] # get nums1 back
#         nums2 = [num[0] for num in nums2]
#         max_score = 0
#         for i in range(len(nums2)-k+1):
#             tmp = nums1[i+1:]
#             heapq.heapify(tmp)
#             for _ in range(len(tmp)-(k-1)):
#                 heapq.heappop(tmp)
#             score = (nums1[i] + sum(tmp)) * nums2[i]
#             max_score = max(max_score, score)
#         return max_score

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(zip(nums1, nums2))
        pairs = sorted(pairs, key=lambda p:p[1],reverse=True)
        n1_sum = 0 # track max
        max_score = 0
        heap = []
        for n1,n2 in pairs:
            if len(heap) == k:
                val = heapq.heappop(heap)
                n1_sum -= val
            heapq.heappush(heap, n1)
            n1_sum += n1
            if len(heap) == k:
                score = n1_sum * n2
                max_score = max(max_score, score)
        return max_score