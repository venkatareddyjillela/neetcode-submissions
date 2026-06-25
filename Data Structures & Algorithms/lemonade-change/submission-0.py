class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        coins = [20, 10, 5]
        for bill in bills:
            change[bill] += 1
            balance = bill - 5
            i = 0
            while balance:
                if i == len(coins):
                    return False
                if (not change[coins[i]]) or (balance - coins[i] < 0):
                    i += 1
                else:
                    balance -= coins[i]
                    change[coins[i]] -= 1
        return True
