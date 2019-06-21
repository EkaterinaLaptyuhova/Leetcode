class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        tail = 0
        i = 0
        n = 0
        d = dict()
        while head < len(s):
            if s[head] not in d:
                d[s[head]] = 1
                head += 1
                i += 1
                n = max(n, i)
            else:
                del d[s[tail]]
                tail += 1
                i -= 1

        return n


solution = Solution()
print(solution.lengthOfLongestSubstring("aaaaacda"))
