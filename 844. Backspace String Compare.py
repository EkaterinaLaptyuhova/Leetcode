class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        k = 0
        n = len(S) - 1
        m = len(T) - 1

        while n > 0 or m > 0:
            if S[n] == T[m] and S[n] != "#":
                n -= 1
                m -= 1

            elif S[n] != "#" and T[m] != "#" and S[n] != T[m]:
                return False

            else:
                while S[n] == "#":
                    n -= 1
                    k += 1

                while k > 0 and n >= 0:
                    if S[n] != '#':
                        n -= 1
                        k -= 1
                    else:
                        n -= 1
                        k += 1

                while T[m] == "#":
                    m -= 1
                    k += 1

                while k > 0 and m >= 0:
                    if k > m and n >= 0:
                        return False
                    elif T[m] != '#':
                        m -= 1
                        k -= 1
                    else:
                        m -= 1
                        k += 1

        return True


solution = Solution()
print(solution.backspaceCompare("y#fo##f", "y#f#o##f"))



