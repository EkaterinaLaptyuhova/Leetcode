from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        n = 0
        k = 0
        while i < len(nums):
            if nums[i] == 1:
                k += 1
                n = max(n, k)
                i += 1
            else:
                k = 0
                i += 1
        return n


solution = Solution()
print(solution.findMaxConsecutiveOnes([0, 0]))

