from typing import List


class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        proceed = True
        r = c = 0

        def is_in_bounds(r, c):
            return 0 <= r < len(room) and 0 <= c < len(room[0])

        cleaned = set()
        while proceed:
            prev_pos = (r, c)
            # right
            while is_in_bounds(r, c) and room[r][c] == 0:
                cleaned.add((r, c))
                c += 1
            c -= 1
            r += 1
            # go down
            while is_in_bounds(r, c) and room[r][c] == 0:
                cleaned.add((r, c))
                r += 1
            r -= 1
            c -= 1
            # go left
            while is_in_bounds(r, c) and room[r][c] == 0:
                cleaned.add((r, c))
                c -= 1
            c += 1
            r -= 1
            # go up
            while is_in_bounds(r, c) and room[r][c] == 0:
                cleaned.add((r, c))
                r -= 1
            r += 1
            c += 1
            if (r, c) == prev_pos:
                proceed = False

        return len(cleaned)


sol = Solution()
print(sol.numberOfCleanRooms([[0, 0, 0], [1, 1, 0], [0, 0, 0]]))  # Output: 7
