from collections import deque
from typing import List


def findWinningPlayer(self, skills: List[int], k: int) -> int:
    n = len(skills)
    queue = deque(range(n))
    current_winner = queue.popleft()
    consecutive_wins = 0

    max_skill = max(skills)

    while consecutive_wins < k:
        challenger = queue.popleft()
        if skills[current_winner] > skills[challenger]:
            consecutive_wins += 1
            queue.append(challenger)
        else:
            queue.append(current_winner)
            current_winner = challenger
            consecutive_wins = 1

        if skills[current_winner] == max_skill:
            break

    return current_winner


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # fill with zero
        dp = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        answer = 1
        # a 2-d tablu I think
        for i in range(1, n):
            for j in range(k + 1):
                dp[i][j] = 1
                for border in range(i):
                    if nums[border] == nums[i]:
                        dp[i][j] = max(dp[i][j], dp[border][j] + 1)
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[border][j - 1] + 1)

                answer = max(answer, dp[i][j])

        return answer


sol = Solution()
print(sol.maximumLength(nums=[1, 2, 1, 1, 3], k=2))  # -> 4
print(sol.maximumLength([1, 2, 3, 4, 5, 1], 0))  # -> 2
