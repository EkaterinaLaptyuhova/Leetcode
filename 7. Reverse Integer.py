"""
def reverse(x):
    k = len(str(x)) - 1
    data_str = str(x)
    new_data = ''
    if data_str[0] == '-':
        new_data = '-'
        while k > 0:
            new_data = new_data + data_str[k]
            k -= 1
    else:
        while k >= 0:
            new_data = new_data + data_str[k]
            k -= 1
    if 2 ** 31 - 1 <= int(new_data) or int(new_data) <= (- 2) ** 31:
        print(0)
    else:
        print(int(new_data))


number = input("Please, write a number: ")
reverse(number)
"""


def reverse_int(x):
    y = 0
    k = 0
    if x < 0:
        x = x * (- 1)
        k = 1
    while x // 10 != 0:
        if x % 10 == 0:
            y = y * 10
            x = x // 10
        else:
            y = y * 10 + (x % 10)
            x = x // 10
    y = y * 10 + x
    if k == 1:
        y = y * (- 1)
    if 2 ** 31 - 1 <= y or y <= (- 2) ** 31:
        print(0)
    else:
        print(y)


reverse_int(1534236469)
