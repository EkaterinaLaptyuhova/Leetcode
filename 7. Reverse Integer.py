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
