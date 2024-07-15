class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        memo = {}

        def dfs(i, vowel):
            if (i, vowel) in memo:
                return memo[(i, vowel)]
            total = 1
            if i > 1:
                if vowel == 'a':
                    total = (dfs(i - 1, 'e') + dfs(i - 1, 'i') + dfs(i - 1, 'u')) % MOD
                elif vowel == 'e':
                    total = (dfs(i - 1, 'a') + dfs(i - 1, 'i')) % MOD
                elif vowel == 'i':
                    total = (dfs(i - 1, 'e') + dfs(i - 1, 'o')) % MOD
                elif vowel == 'o':
                    total = dfs(i - 1, 'i')
                else:
                    total = (dfs(i - 1, 'i') + dfs(i - 1, 'o')) % MOD
            memo[(i, vowel)] = total
            return total

        return sum(dfs(n, vowel) for vowel in 'aeiou') % MOD


sol = Solution()
print(sol.countVowelPermutation(1))  # -> 5
print(sol.countVowelPermutation(2))  # -> 10
