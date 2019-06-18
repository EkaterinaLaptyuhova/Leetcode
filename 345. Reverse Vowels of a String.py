class Solution:
    def reverseVowels(self, s: str) -> str:
        m = 0
        n = len(s) - 1
        vowels = "AEOUIaeoui"

        while m < n:
            if s[m] in vowels:
                if s[n] in vowels:
                    element = s[m]
                    reverse_element = s[n]
                    s = s[: m] + reverse_element + s[m + 1 : n] + element + s[n + 1 : ]
                    m += 1
                    n -= 1
                else:
                    n -= 1
            else:
                m += 1
        return s
