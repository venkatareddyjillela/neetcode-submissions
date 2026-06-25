class Solution:
    def checkValidString(self, s: str) -> bool:
        # openN = 0
        # closeN = 0
        # starN = 0

        # for ch in s:
        #     if ch == '(':
        #         openN += 1
        #     elif ch == ')':
        #         closeN += 1
        #     else:
        #         starN += 1
            
        #     if closeN > openN:
        #         starN -= 1
        #         if starN < 0:
        #             return False
        #         closeN += 1
        
        # if openN > closeN:
        #     starN -= (openN - closeN)
        
        # return False if starN < 0 else True

        leftMin, leftMax = 0, 0
        for ch in s:
            if ch == '(':
                leftMin += 1
                leftMax += 1
            elif ch == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMin < 0:
                leftMin = 0

            if leftMax < 0:
                return False
        
        return False if leftMin > 0 else True