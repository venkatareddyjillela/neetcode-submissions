class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        emailToAcc = {}
        
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        email_group = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            email_group[leader].append(e)

        res = []
        for i, emails in email_group.items():
            name = accounts[i][0]
            res.append([name] + sorted(email_group[i]))

        return res