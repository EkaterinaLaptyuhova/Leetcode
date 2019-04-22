class Solution:
    def reverseWords(self, s: str) -> str:
        n = 0
        word = ''
        new_str = ''
        while n < len(s):
            if s[n] == ' ':
                n += 1
            else:
                while n < len(s) and s[n] != " ":
                    word = word + s[n]
                    n += 1
                if new_str == '':
                    new_str = word
                else:
                    new_str = word + " " + new_str
                word = ''
        return new_str