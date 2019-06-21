from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[i] += 1
        if digits[i] == 10:
            while i > 0:
                if digits[i] == 10:
                    digits[i] = 0
                    i -= 1
                    digits[i] += 1
                else:
                    return digits
            if digits[0] == 10:
                digits[0] = 0
                digits = [1] + digits
        return digits


solution = Solution()
print(solution.plusOne([9, 9, 9]))
