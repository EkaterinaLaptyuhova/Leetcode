class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        power = 0
        while 4 ** power <= num:
            if num == 4 ** power:
                return True
            power += 1
        return False


