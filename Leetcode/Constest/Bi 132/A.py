from collections import deque
from typing import List


class Solution:
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


# Test cases
sol = Solution()
print(sol.findWinningPlayer([4, 2, 6, 3, 9], 2))  # Output: 2
print(sol.findWinningPlayer([2, 5, 4], 3))  # Output: 1
print(sol.findWinningPlayer([16, 4, 7, 17], 562084119))  # Output: 3
