class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)
        self.count = 0                                        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for followerId in self.users[userId]:
            if followerId in self.tweets:
                tweets.extend(self.tweets[followerId])
        tweets.extend(self.tweets[userId])  
        heapq.heapify(tweets)
        res = []
        while tweets and len(res) < 10:
            res.append(heapq.heappop(tweets)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
