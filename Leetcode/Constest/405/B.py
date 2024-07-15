from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]

        def is_valid(s):
            for i in range(len(s) - 1):
                if s[i] == '0' and s[i + 1] == '0':
                    return False
            return True

        def dfs(current, n):
            if len(current) == n:
                return [current] if is_valid(current) else []

            return dfs(current + '0', n) + dfs(current + '1', n)

        return dfs('', n)


sol = Solution()
print(sol.validStrings(3))
print(sol.validStrings(1))
print(sol.validStrings(4))
