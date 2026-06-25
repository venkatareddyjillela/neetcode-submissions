class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        
        return self.par[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        if self.rank[root_x] > self.rank[root_y]:
            self.par[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.par[root_x] = root_y
        else:
            self.par[root_y] = root_x
            self.rank[root_x] += 1



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        emailToAcc = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    uf.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        
        emailGroups = defaultdict(list)
        for email, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroups[leader].append(email)
        
        res = []
        for i, emails in emailGroups.items():
            name = accounts[i][0]
            new_account = [name]
            new_account.extend(sorted(emails))
            res.append(new_account)
        
        return res
