import collections


class Solution:
    def compressedString(self, word: str) -> str:
        # freq = collections.Counter(word)
        # answer = []
        # for k, v in freq.items():
        #     if v > 9:
        #         answer.append(f'9{k}' * (v // 9))
        #     if (v % 9) != 0:
        #         answer.append(str((v % 9)) + k)
        # return ''.join(answer)
        comp = ""
        i = 0
        while i < len(word):
            c = word[i]
            count = 0
            while i < len(word) and word[i] == c and count < 9:
                count += 1
                i += 1
            comp += str(count) + c
        return comp


s = Solution()
print(s.compressedString('aaaaaaaaaaaaaabb'))  # -> "9a5a2b"
print(s.compressedString('abcde'))
