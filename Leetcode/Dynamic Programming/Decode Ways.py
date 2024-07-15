class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s) - 1:
                return 1
            answer = dfs(i + 1)
            if s[i: i + 2] <= '26':
                answer += dfs(i + 2)
            memo[i] = answer
            return answer

        if s == '0':
            return 0
        return dfs(0)



sol = Solution()
print(sol.numDecodings('12'))  # -> 2
print(sol.numDecodings('226'))  # -> 3
