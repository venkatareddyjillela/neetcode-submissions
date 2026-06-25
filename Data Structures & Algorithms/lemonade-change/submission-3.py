class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # change = defaultdict(int)
        # coins = [10, 5]
        # for bill in bills:
        #     change[bill] += 1
        #     balance = bill - 5
        #     i = 0
        #     while balance:
        #         if i == len(coins):
        #             return False
        #         if (not change[coins[i]]) or (balance - coins[i] < 0):
        #             i += 1
        #         else:
        #             balance -= coins[i]
        #             change[coins[i]] -= 1
        # return True

        five, ten = 0, 0

        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                ten += 1
                if not five:
                    return False
                five -= 1
            else:
                balance = b - 5
                if ten:
                    balance -= 10
                    ten -= 1
                while balance:
                    if not five:
                        return False
                    balance -= 5
                    five -= 1
        
        return True
                    
                    
                    
