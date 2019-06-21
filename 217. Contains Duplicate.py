from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i = 0
        d = dict()
        while i < len(nums):
            if nums[i] not in d:
                d[nums[i]] = 1
                i += 1
            else:
                return True
        return False


solution = Solution()
print(solution.containsDuplicate([1,2,3,4]))
