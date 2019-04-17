class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        while 2 ** power <= n:
            if n == 2 ** power:
                return True
            else:
                power += 1
        return False


solution = Solution()
print(solution.isPowerOfTwo(5))