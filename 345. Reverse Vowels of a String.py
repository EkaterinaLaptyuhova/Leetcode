class Solution:
    def reverseVowels(self, s: str) -> str:    
        n = 0
        k = 0
        m = len(s) - 1
        new_s = ''
        vowels = 'aeiouAEIOU'
        while n < len(s) and m >= -1:
            consonant = True
            while k < len(vowels):
                if s[n] != vowels[k]:
                    k += 1
                else:
                    consonant = False
                    k = 0
                    break

            if consonant:
                    new_s = new_s + s[n]
                    n += 1
                    k = 0
            else:
                consonant_m = True
                while k < len(vowels):
                    if s[m] != vowels[k]:
                        k += 1
                    else:
                        consonant_m = False
                        k = 0
                        break
                k = 0

                if consonant_m:
                    m -= 1
                else:
                    new_s = new_s + s[m]
                    m -= 1
                    n += 1
        return new_s