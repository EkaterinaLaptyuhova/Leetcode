from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = len(nums) - 1
        while i >= 0:
            if target - nums[i] in nums[: i]:
                return nums.index(target - nums[i]), i
            else:
                i -= 1


solution = Solution()
print(solution.twoSum([3, 2, 4], 6))

