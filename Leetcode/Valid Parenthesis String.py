# 678. Valid Parenthesis String
class Solution:
    def checkValidString(self, s: str) -> bool:
        open, close = 0, 0
        left, right = 0, len(s) - 1

        while left <= len(s) - 1 and right >= 0:
            # if we see an open brocket increase the count of the opens
            if s[left] == '(' or s[left] == '*':
                open += 1
            # otherwise we decrease the count of close, it can mimic that
            # there is a match for the open
            else:
                open -= 1
            if s[right] == ')' or s[right] == '*':
                close += 1
            else:
                close -= 1
            # if any of the counters become zero the answer is False
            if open < 0 or close < 0:
                return False
            left += 1
            right -= 1

        return True


sol = Solution()
# print(sol.checkValidString('***)'))
print(sol.checkValidString('((*))()'))
print(sol.checkValidString('('))
