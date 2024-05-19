def max_energy(energy, k):
    # maybe we use recursion???

    def max_energy_helper(i, dp):
        if i >= len(energy):
            return 0
        if dp[i] != -1001:
            return dp[i]
        dp[i] = energy[i] + max_energy_helper(i + k, dp)
        return dp[i]

    # using the biggest number that input gives me
    dp = [-1001] * (len(energy) + 1)
    return max(max_energy_helper(i, dp) for i in range(len(energy)))


print(max_energy([5, 2, -10, -5, 1], 3))
print(max_energy([-2, -3, -1], 2))
print(max_energy([2, 5, 10, 11, 1, 10, 2, -50], 2))
# sol = Solution()
# # print(sol.maximumEnergy(energy=[5, 2, -10, -5, 1], k=3))  # Output: 3
# # print(sol.maximumEnergy(energy=[-2, -3, -1], k=2))  # Output: -1
# print(sol.maximumEnergy([2, 5, 10, 11, 1, 10, 2, -50], 2))
