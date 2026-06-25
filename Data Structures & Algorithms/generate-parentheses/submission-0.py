from collections import defaultdict
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        close_ = 0
        open_ = 0
        res = ''
        count = 0
        self.generate_all_possibilities(count, n, open_, close_, res, output)
        return output

    def generate_all_possibilities(self, count, n, open_, close_, res, output):
        # if count == 2 * n:
        #     return ''
        if close_ > open_:
            return ''
        if len(res) == 2 * n:
            print(res)
            if self.isValid(res):
                output.append(res)
            return ''

        return self.generate_all_possibilities(count+1, n, open_+1, close_, res + '(', output) + self.generate_all_possibilities(count+1, n, open_, close_+1, res + ')', output)
        


        

    def isValid(self, s: str) -> bool:
        par_map = {
            ")": "("
        }
        count = defaultdict(int)
        for par in s:
            if par not in par_map:
                count[par] += 1
            else:
                if count[par_map[par]] < 1:
                    return False
                count[par_map[par]] -= 1
        
        return sum(count.values()) == 0