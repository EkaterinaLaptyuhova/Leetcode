class Solution:
    def reverseString(self, s: List[str]) -> None:
        m = 0
        n = len(s) - 1
        while m < n:
            element = s[m]
            reverse_element = s[n]
            s[m] = reverse_element
            s[n] = element
            m += 1
            n -= 1
