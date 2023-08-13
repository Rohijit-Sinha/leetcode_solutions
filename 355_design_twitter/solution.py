from typing import List
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.count = 0
        self.follow_map = defaultdict(set) # set[ID]
        self.tweet_map = defaultdict(list) # List[(count, tweetID)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        minHeap.extend(self.tweet_map[userId])
        for followee in self.follow_map[userId]:
            minHeap.extend(self.tweet_map[followee])
        heapq.heapify(minHeap)
        for _ in range(10):
            if not minHeap:
                break
            res.append(heapq.heappop(minHeap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)