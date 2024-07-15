from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)

        def backtrack(start, i, cur):
            if i == len(s):
                if len(''.join(cur)) == len(s):
                    res.append(' '.join(cur))
                return

            backtrack(start, i + 1, cur)  # don't consider it
            if s[start: i + 1] in wordDict:
                cur.append(s[start:i + 1])
                backtrack(i + 1, i + 1, cur)  # consider it
                cur.pop()

        backtrack(0, 0, [])
        return res


sol = Solution()
print(
    sol.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))  # -> ["cats and dog","cat sand dog"]
