from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_1, candidate_2 = None, None
        count_1, count_2 = 0, 0

        for num in nums:
            if candidate_1 == num:
                count_1 += 1
            elif candidate_2 == num:
                count_2 += 1
            elif count_1 == 0:
                candidate_1, count_1 = num, 1
            elif count_2 == 0:
                candidate_2, count_2 = num, 1
            else:
                count_1 -= 1
                count_2 -= 1

        # We need to verify if our candidates are indeed majority elements
        count_1, count_2 = 0, 0
        for num in nums:
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 += 1

        result = []
        if count_1 > len(nums) // 3:
            result.append(candidate_1)
        if count_2 > len(nums) // 3:
            result.append(candidate_2)

        return result

# Example test cases
sol = Solution()
print(sol.majorityElement([3, 2, 3]))  # -> [3]
print(sol.majorityElement([1, 2]))  # -> [1, 2]
print(sol.majorityElement([1]))  # -> [1]
