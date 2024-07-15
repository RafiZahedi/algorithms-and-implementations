class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        i = 0

        while i < len(s):
            if s[i].isdigit():
                for j in range(i - 1, -1, -1):
                    if not s[j].isdigit():
                        s.pop(j)
                        # no need to continue I think
                        break
                s.pop(i - 1)
                i -= 1
            else:
                i += 1

        return ''.join(s)

sol = Solution()
print(sol.clearDigits('abs'))