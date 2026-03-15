# https://leetcode.com/problems/design-twitter/description/

import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:

        # merge K sorted Lists

        res = []  # List to store the 10 most recent tweets
        minHeap = []

        # Get all followees + self
        followee_set = self.followMap[userId] | {userId}

        for followeeId in followee_set:
            tweets = self.tweetMap[followeeId]
            if tweets:
                idx = len(tweets) - 1
                count, tweetId = tweets[idx]
                # Push [count, tweetId, followeeId, next index to check]
                minHeap.append([count, tweetId, followeeId, idx - 1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                next_count, next_tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minHeap, [next_count, next_tweetId, followeeId, idx - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:

        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:

        # check if the followeeId is following followerId
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
