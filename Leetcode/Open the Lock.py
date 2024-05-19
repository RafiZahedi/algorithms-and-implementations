# 752. Open the Lock
from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Initialize the set of dead ends
        deadends = set(deadends)

        # Initialize the queue for BFS
        queue = deque([('0000', 0)])

        # Initialize a set to keep track of visited combinations
        visited = set(['0000'])

        # Perform BFS
        while queue:
            current, steps = queue.popleft()

            # Check if the current combination is the target
            if current == target:
                return steps

            if current in deadends:
                continue

            # Generate next possible combinations by rotating each wheel
            for i in range(4):
                for d in [-1, 1]:
                    next_combination = current[:i] + str((int(current[i]) + d) % 10) + current[i + 1:]

                    # Check if the next combination has not been visited and is not a dead end
                    if next_combination not in visited and next_combination not in deadends:
                        queue.append((next_combination, steps + 1))
                        visited.add(next_combination)

        # If target is not reachable
        return -1


sol = Solution()
print(sol.openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))  # -> 6
