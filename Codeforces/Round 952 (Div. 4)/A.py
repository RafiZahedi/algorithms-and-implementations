import math


def solve(x: int, y: int, z: int, k: int) -> int:
    answer = 0

    for a in range(1, int(math.cbrt(k)) + 1):
        if k % a == 0:
            for b in range(1, int(math.sqrt(k // a)) + 1):
                if (k // a) % b == 0:
                    c = k // (a * b)
                    if (a <= x and b <= y and c <= z):
                        answer = max(answer, (x - a + 1) * (y - b + 1) * (z - c + 1))
                    # Check for other arrangements of a, b, and c
                    answer = max(answer, (x - a + 1) * (y - c + 1) * (z - b + 1))
                    answer = max(answer, (x - b + 1) * (y - a + 1) * (z - c + 1))
                    answer = max(answer, (x - b + 1) * (y - c + 1) * (z - a + 1))
                    answer = max(answer, (x - c + 1) * (y - a + 1) * (z - b + 1))
                    answer = max(answer, (x - c + 1) * (y - b + 1) * (z - a + 1))

    return answer


def main():
    test_cases = int(input())
    results = []

    for _ in range(test_cases):
        x, y, z, k = map(int, input().split())
        results.append(solve(x, y, z, k))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
