class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for followeeId in self.users[userId]:
            if followeeId in self.tweets:
                feed.extend(self.tweets[followeeId])
        feed.extend(self.tweets[userId])
        heapq.heapify(feed)
        res = []
        while feed and len(res) < 10:
            res.append(heapq.heappop(feed)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in  self.users[followerId]:
            self.users[followerId].remove(followeeId)
