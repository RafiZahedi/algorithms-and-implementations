from collections import deque


class State:
    def __init__(self, pos, swim):
        self.pos = pos
        self.swim = swim


def solve():
    n, m, k = map(int, input().split())
    string = input().strip()

    seen = [False] * (n + 2)
    q = deque([State(0, 0)])
    seen[0] = True

    flag = False

    while not flag and q:
        current = q.popleft()

        pos = current.pos
        move = current.swim
        # if at start or behind is not 'L'
        if pos == 0 or string[pos - 1] == 'L':
            for i in range(1, m + 1):
                new = pos + i
                if new == n + 1:
                    flag = True
                    break
                if new <= n and string[new - 1] != 'C' and not seen[new]:
                    seen[new] = True
                    q.append(State(new, move))
        # if we can still move, and correct position we have
        if 0 < pos <= n and string[pos - 1] == 'W' and move < k:
            new = pos + 1
            # if out of bond then break
            if new == n + 1:
                flag = True
                break
            if new <= n and string[new - 1] != 'C' and not seen[new]:
                seen[new] = True
                q.append(State(new, move + 1))

    print("YES" if flag else "NO")


for _ in range(int(input())):
    solve()
