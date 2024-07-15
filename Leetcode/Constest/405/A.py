from typing import List


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        res = []

        for i in range(n):
            index = (i + k) % n
            res.append(s[index])

        return ''.join(res)


sol = Solution()
print(sol.getEncryptedString(s="dart", k=3))
print(sol.getEncryptedString('aaa', 1))