def solve():
    def is_possible(a, k):
        N = len(a)
        # dp of size n, initially zero
        dp = [0] * N
        for right in range(N - k + 1):
            now = a[right]
            reverse = 0
            if right > 0:
                reverse += dp[right - 1]
            point = max(0, right - k + 1)
            if point > 0:
                reverse -= dp[point - 1]
            if reverse % 2:
                now = 1 - now
            if right > 0:
                dp[right] = dp[right - 1]
            if now == 0:
                dp[right] += 1

        for right in range(N - k + 1, N):
            dp[right] = dp[right - 1]
            now = a[right]
            reverse = dp[right - 1]
            point = max(0, right - k + 1)

            if point > 0:
                reverse -= dp[point - 1]

            if reverse % 2:
                now = 1 - now

            if not now:
                return False
        return True

    n = int(input())
    nums = [0] * n
    input_sttring = input()

    for i in range(n):
        if input_sttring[i] == '1':
            nums[i] = 1

    for k in range(n, 0, -1):
        if is_possible(nums, k):
            return k


for _ in range(int(input())):
    print(solve())
