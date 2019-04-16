class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        k = 1
        str_represent = []
        while k <= n:
            if k % 3 == 0 and k % 5 == 0:
                str_represent.append('FizzBuzz')
                k += 1
            elif k % 3 == 0:
                str_represent.append('Fizz')
                k += 1
            elif k % 5 == 0:
                str_represent.append('Buzz')
                k += 1
            else:
                str_represent.append(str(k))
                k += 1
        return str_represent


