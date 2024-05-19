import collections
import heapq


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        ring_len = len(ring)
        key_len = len(key)

        # Index of occurrences of each char
        char_indexes = collections.defaultdict(list)
        for i, char in enumerate(ring):
            char_indexes[char].append(i)

        # we use Dijkstra algorithm
        heap = [(0, 0, 0)]  # steps, ring index, key index
        seen = set()

        while heap:
            steps, ring_index, key_index = heapq.heappop(heap)

            # if we spelled the key word all
            if key_index == key_len:
                break

            if (ring_index, key_index) in seen:
                continue
            seen.add((ring_index, key_index))

            # for other occurrences
            for next_index in char_indexes[key[key_index]]:
                heapq.heappush(heap, (steps + count_steps(ring_index, next_index), next_index, key_index + 1))

        # we always have to press the button for each key
        # so the answer always will have the +len(key)
        return steps + key_len


sol = Solution()
print(sol.findRotateSteps('godding', 'gd'))  # -> 4
print(sol.findRotateSteps('godding', 'godding'))  # -> 13
