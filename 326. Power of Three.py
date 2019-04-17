class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power = 0
        while 3 ** power <= n:
            if n == 3 ** power:
                return True
            else:
                power += 1
        return False
